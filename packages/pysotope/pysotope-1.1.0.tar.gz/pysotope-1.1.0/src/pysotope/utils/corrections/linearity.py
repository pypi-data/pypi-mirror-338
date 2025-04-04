# -*- coding: utf-8 -*-
import pandas as pd
from . .queries import *
from . .queries import neg_response
from . .figures import *
from IPython.display import clear_output
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from . .curve_fitting import *

def lin_response(log_file_path):
    valid_responses = ['yes', 'y', 'true', 't', 'no', 'n', 'false', 'f']
    while True:
        response = input("\nAssign a linearity correction? (Y/N)\n").lower()
        if response in valid_responses:
            append_to_log(log_file_path, "Linearity application application: "+str(response))
            return response
        else:
            print("\nInvalid response. Try again.\n")

def process_linearity_correction(samp, drift, lin_std, user_choice, correction_log, folder_path, fig_path, isotope, user_linearity_conditions, log_file_path):
    ex = pd.DataFrame()
    dD_id = 'drift_corrected_dD' if correction_log.loc["Drift","samples"] == 1 else "dD"
    # Normalize data
    norm=pd.DataFrame()
    mean_isotope_dict={}
    for i in ["C20","C28"]:
        mask = lin_std.chain==i
        temp = lin_std.loc[mask, ['area','chain',dD_id]].copy()
        mean_isotope_dict[i] = temp[dD_id].mean()
        #temp[user_choice] -= temp[user_choice].mean() # For gls regression
        temp[user_choice] -= temp[user_choice].min()-1
        norm = pd.concat([norm, temp])
    response = lin_response(log_file_path)
    if neg_response(response):
        print("\nSkipping linearity correction.\n")
        return samp, correction_log, lin_std, drift
    else:
        if user_linearity_conditions:
            while True:
                chain_corr_val = input("\nEnter peak area cutoff value for C_{20} and C_{28} linearity stds\n")
                try:
                    chain_corr_vals = [float(num) for num in chain_corr_val.split()]  # Split the input string into a list
                    if len(chain_corr_vals) == 1:
                        correction_log.loc["Linearity"] = chain_corr_vals[0]  # Save the single value
                        break  # Break the loop since the condition is met
                    else:
                        print("Please enter one number.\n")
                except ValueError:
                    print("Invalid input. Please enter a numerical value.\n")
        else:
            chain_corr_val = 0
            correction_log.loc["Linearity"] = chain_corr_val
    chain_corr_val = float(chain_corr_val)
    verify_lin_plot(norm, fig_path, dD_id,log_file_path, cutoff_line=chain_corr_val, isotope=isotope)

    user_input = input("\nDoes this look correct? (Y/N)\n").lower()
    if pos_response(user_input):
        append_to_log(log_file_path, "Minimum peak area to derive linearity correction: "+str(chain_corr_val))
        lin_std, drift, samp, excluded_drift, excluded_lin_std, excluded_samp  = linearity_correction(drift, samp, lin_std, norm, chain_corr_val, dD_id, folder_path, fig_path, log_file_path=log_file_path)
        append_to_log(log_file_path, "Number of drift standards excluded because of below threshold area: "+str(len(excluded_drift)))
        append_to_log(log_file_path, "Number of linearity standards excluded because of below threshold area: "+str(len(excluded_lin_std)))
        append_to_log(log_file_path, "Number of samples excluded because of below threshold area: "+str(len(excluded_samp)))
        # Save excluded samples if any
        if not excluded_drift.empty or not excluded_lin_std.empty or not excluded_samp.empty:
            subfolder = create_subfolder(folder_path, "Excluded_Data")
            if not excluded_drift.empty:
                excluded_drift.to_csv(os.path.join(subfolder, 'Drift_standards_excluded_peak_area.csv'), index=False)
            if not excluded_lin_std.empty:
                excluded_lin_std.to_csv(os.path.join(subfolder, 'Linearity_standards_excluded_peak_area.csv'), index=False)
            if not excluded_samp.empty:
                excluded_samp.to_csv(os.path.join(subfolder, 'Samples_excluded_by_peak_area.csv'), index=False)
            #log_excluded_samples(subfolder, excluded_drift, excluded_lin_std, excluded_samp)

        clear_output(wait=True)
        return drift, correction_log, lin_std, samp

    elif neg_response(user_input):
        print("\nSkipping linearity correction.\n")
        time.sleep(0)  # Wait for 1 second
        clear_output(wait=True)
        return drift, correction_log, lin_std, samp

    else:
        time.sleep(0)
        clear_output(wait=True)
        print("\nInvalid response. Try again.\n")

# def linearity_correction(drift, samp, lin_std, lin_norm, area_cutoff, dD_id, folder_path, fig_path, log_file_path, fig=False):
#     area_cutoff = float(area_cutoff)
#     corrected_drift = pd.DataFrame()  # Initialize an empty DataFrame to store corrected unknown
#
#     # Filter linearity standards and unknown based on area cutoff
#     mask                   = lin_norm['area'] >= area_cutoff
#     filtered_lin_norm      = lin_norm[mask] # normalized linearity standards
#     filtered_lin_std       = lin_std[mask]  # original linearity standards
#     filtered_drift         = drift[drift['area'] >= area_cutoff]
#
#     # Store and remove excluded unknown
#     excluded_drift = drift[drift['area']<area_cutoff]
#     excluded_lin_std = lin_std[lin_std['area']<area_cutoff]
#     excluded_samp = samp[samp['area'] < area_cutoff]
#
#     # Store and remove excluded unknown
#     xdata = filtered_lin_norm['area'].to_numpy()
#     ydata = filtered_lin_norm[dD_id].to_numpy()
#     best_model, popt, sse, pcov = fit_and_select_best(xdata, ydata)
#     pred_error = prediction_std(best_model, xdata, popt, pcov)
#     # Generate fitted predictions from the chosen model
#     if best_model == "exponential":
#         y_fit = exp_func(xdata, *popt)
#     else:
#         y_fit = log_func(xdata, *popt)
#
#     # Total Sum of Squares
#     tss = np.sum((ydata - ydata.mean()) ** 2)
#     if tss == 0:
#         r_squared = 1.0  # Degenerate case if data is all the same
#     else:
#         r_squared = 1 - (sse / tss)
#
#     print(f"Chosen Model: {best_model}")
#     print(f"Parameters: {popt}")
#     print(f"SSE: {sse:.3f}, R²: {r_squared:.3f}")
#
#     lin_top_sort = filtered_lin_norm.sort_values(by='area', ascending=False)
#     top_count = max(int(len(lin_top_sort) * 0.2), 1)  # ensure at least 1 point
#     lin_top_qt_area = lin_top_sort.head(top_count)
#     lin_reference = lin_top_qt_area[dD_id].mean()  # average δD of top 20%
#
#     # Combine new fit (y_fit) with the old reference approach
#     lin_cor = y_fit - lin_reference + filtered_lin_norm[dD_id]
#     filtered_lin_std['linearity_corrected_dD'] = lin_cor
#     filtered_lin_std['linearity_error'] = pred_error  # or calculate a custom uncertainty
#
#     # Apply to drift
#     if best_model == "exponential":
#         drift_est = exp_func(np.array(filtered_drift.area), *popt)
#     else:
#         drift_est = log_func(np.array(filtered_drift.area), *popt)
#     pred_error = prediction_std(best_model, np.array(filtered_drift.area), popt, pcov)
#     drift_cor = drift_est-lin_reference
#     filtered_drift['linearity_corrected_dD'] = drift_cor[~np.isnan(drift_cor)]#[~drift_cor.isna()]
#     filtered_drift['linearity_error'] = pred_error
#
#     # Apply to samples
#     filtered_samp = samp[samp['area'] >= area_cutoff]
#     if best_model == "exponential":
#         samp_est = exp_func(np.array(filtered_samp.area), *popt)
#     else:
#         samp_est = log_func(np.array(filtered_samp.area), *popt)
#     pred_error = prediction_std(best_model, np.array(filtered_samp.area), popt, pcov)
#
#     samp_cor = samp_est-lin_reference
#     samp_cor = samp_cor+filtered_samp[dD_id]
#     filtered_samp['linearity_corrected_dD'] = samp_cor[~samp_cor.isna()]
#     filtered_samp['linearity_error'] = pred_error
#
#     return filtered_lin_std, filtered_drift, filtered_samp, excluded_drift, excluded_lin_std, excluded_samp

def linearity_correction(drift, samp, lin_std, lin_norm, area_cutoff, dD_id, folder_path, fig_path, log_file_path, fig=False):
    area_cutoff = float(area_cutoff)
    corrected_drift = pd.DataFrame()  # Initialize an empty DataFrame to store corrected unknown

    # Filter linearity standards and unknown based on area cutoff
    mask              = lin_norm['area'] >= area_cutoff
    filtered_lin_norm = lin_norm[mask].copy()  # copy to avoid SettingWithCopy warning
    filtered_lin_std  = lin_std[mask].copy()
    filtered_drift    = drift[drift['area'] >= area_cutoff].copy()

    # Store excluded data
    excluded_drift   = drift[drift['area'] < area_cutoff]
    excluded_lin_std = lin_std[lin_std['area'] < area_cutoff]
    excluded_samp    = samp[samp['area'] < area_cutoff]

    # ----------------- Fit Models and Select Best -----------------
    xdata = filtered_lin_norm['area'].to_numpy()
    ydata = filtered_lin_norm[dD_id].to_numpy()
    best_model, popt, sse, pcov = fit_and_select_best(xdata, ydata)
    pred_error = prediction_std(best_model, xdata, popt, pcov)
    print(popt)
    # Generate fitted predictions from the chosen model
    if best_model == "linear":
        y_fit = linear_func(xdata, *popt)
    else:  # best_model == "log"
        y_fit = log_func(xdata, *popt)

    # Total Sum of Squares and R²
    tss = np.sum((ydata - ydata.mean()) ** 2)
    if tss == 0:
        r_squared = 1.0
    else:
        r_squared = 1 - (sse / tss)

    print(f"Chosen Model: {best_model}")
    print(f"Parameters: {popt}")
    print(f"SSE: {sse:.3f}, R²: {r_squared:.3f}")

    # Determine reference value from the top 20% (by area) of the linearity standards
    lin_top_sort = filtered_lin_norm.sort_values(by='area', ascending=False)
    top_count = max(int(len(lin_top_sort) * 0.2), 1)
    lin_top_qt_area = lin_top_sort.head(top_count)
    lin_reference = lin_top_qt_area[dD_id].mean()  # average δD of top 20%

    # Combine new fit with the old reference approach for linearity standards
    lin_cor = y_fit - lin_reference + filtered_lin_norm[dD_id]
    filtered_lin_std['linearity_corrected_dD'] = lin_cor
    filtered_lin_std['linearity_error'] = pred_error  # or calculate a custom uncertainty

    # Apply correction to drift
    if best_model == "linear":
        drift_est = linear_func(np.array(filtered_drift.area), *popt)
    else:
        drift_est = log_func(np.array(filtered_drift.area), *popt)
    pred_error_drift = prediction_std(best_model, np.array(filtered_drift.area), popt, pcov)
    drift_cor = drift_est - lin_reference
    filtered_drift['linearity_corrected_dD'] = drift_cor[~np.isnan(drift_cor)]
    filtered_drift['linearity_error'] = pred_error_drift

    # Apply correction to samples
    filtered_samp = samp[samp['area'] >= area_cutoff].copy()
    if best_model == "linear":
        samp_est = linear_func(np.array(filtered_samp.area), *popt)
    else:
        samp_est = log_func(np.array(filtered_samp.area), *popt)
    pred_error_samp = prediction_std(best_model, np.array(filtered_samp.area), popt, pcov)
    samp_cor = samp_est - lin_reference + filtered_samp[dD_id]
    filtered_samp['linearity_corrected_dD'] = samp_cor[~samp_cor.isna()]
    filtered_samp['linearity_error'] = pred_error_samp

    return filtered_lin_std, filtered_drift, filtered_samp, excluded_drift, excluded_lin_std, excluded_samp

























