import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# analysis params:
SIGMAS = 5                    # number of sdandard deviation as signal threshold
BASELINE_TRESHOLD = 1         # maximum amplitude of baseline deviation for ROI selection

# timings:
CALM_PERIOD = 10              # time in sec before trigger for baseline
CALM_PERIOD_AFTER_TRIG = 20   # time in sec after trigger for baseline
SKIP_AFTER_APPLICATION = 60   # time to skip in sec after application started

# debug mode
DEBUG = False

# triggers time value in ms:
TODO_LIST_C = [ 

['2024_04_19_C',
    {
    'stim_A' : 32874,
    'stim_C' : 97202,

    'appl_1' : 507193,
    'wout_1' : 983976,

    'appl_2' : 1268045,
    'wout_2' : 1721035,

    'appl_3' : 2318684,
    },],

['2024_04_23_C',
    {
    'stim_A' : 34551,
    'stim_C' : 167665,

    'appl_1' : 534279,
    'wout_1' : 1030543,

    'appl_2' : 1267778,
    'wout_2' : 1819482,

    'appl_3' : 2179672,
    },],

['2024_04_24_M1_C',
    {
    'stim_A' : 35449,
    'stim_C' : 100026,

    'appl_1' : 589977,
    'wout_1' : 792621,

    'appl_2' : 998471,
    'wout_2' : 1223034,

    'appl_3' : 1521751,
    },],

['2024_04_24_M2_C',
    {
    'stim_A' : 59928,
    'stim_C' : 155625,

    'appl_1' : 669896,
    'wout_1' : 957021,

    'appl_2' : 1228097,
    'wout_2' : 1749521,

    'appl_3' : 2112350,
    },],

['2024_04_25_C',
    {
    'stim_A' : 53535,
    'stim_C' : 122560,

    'appl_1' : 597215,
    'wout_1' : 1100744,

    'appl_2' : 1467636,
    'wout_2' : 2119382,

    'appl_3' : 2350874,
    },],

['2024_04_29_C',
    {
    'stim_A' : 47824,
    'stim_C' : 117441,

    'appl_1' : 655962,
    'wout_1' : 903924,

    'appl_2' : 1248345,
    'wout_2' : 1710632,

    'appl_3' : 2038917,
    'last_DRS' : 264195,
    },],

['2024_05_01_C',
    {
    'stim_A' : 84478,
    'stim_C' : 265657,

    'appl_1' : 636790,
    'wout_1' : 944850,

    'appl_2' : 1370577,
    'wout_2' : 1861856,

    'appl_3' : 2184076,
    },],


]

def stable_baseline_creteria(baseline):
    
    # Apply Gaussian smoothing
    sigma = SIGMAS  # Standard deviation for Gaussian kernel
    smoothed_baseline = gaussian_filter1d(baseline, sigma)
    amplitude = np.max(smoothed_baseline) - np.min(smoothed_baseline)
    decision = bool(amplitude < BASELINE_TRESHOLD)
    
    if not decision:
        plt.figure(figsize=(10, 6))
        plt.plot(baseline, label='Original Noisy Sequence')
        plt.plot(smoothed_baseline, label='Smoothed Sequence', linewidth=2)
        plt.legend()
        plt.grid(True)
        plt.savefig('unstable_rois/{}.jpg'.format(np.random.randint(10000)))
        plt.close()

    return decision


def process_csv(input, stim_A, stim_C, appl_1, wout_1, appl_2, wout_2, appl_3, last_DRS=None):

    # Define time ranges
    start_bl_A, end_bl_A   = -CALM_PERIOD+stim_A/1000, -1+stim_A/1000
    start_A, end_A         = -4 +stim_A/1000,  5 +stim_A/1000 

    start_bl_C, end_bl_C   = -CALM_PERIOD+stim_C/1000, -1+stim_C/1000
    start_C, end_C         = -4 +stim_C/1000,  5 +stim_C/1000

    if not last_DRS: last_DRS = end_C

    start_bl_1, end_bl_1   = -CALM_PERIOD+appl_1/1000, CALM_PERIOD_AFTER_TRIG+appl_1/1000
    start_1, end_1 = SKIP_AFTER_APPLICATION+appl_1/1000,    wout_1/1000

    start_bl_2, end_bl_2   = -CALM_PERIOD+appl_2/1000, CALM_PERIOD_AFTER_TRIG+appl_2/1000
    start_2, end_2 = SKIP_AFTER_APPLICATION+appl_2/1000,    wout_2/1000

    start_bl_3, end_bl_3   = -CALM_PERIOD+appl_3/1000, CALM_PERIOD_AFTER_TRIG+appl_3/1000
    start_3, end_3 = SKIP_AFTER_APPLICATION+appl_3/1000, 100000

    # Load the data
    df = pd.read_csv(input + '.csv')
    output = pd.DataFrame()

    # make zero timepoint at the beginning
    time = df.columns[0]
    df[time] = df[time] - df[time].iloc[0] + (df[time].iloc[1] - df[time].iloc[0])

    # for debug:
    if DEBUG:
        fig = plt.figure()
        a1  = fig.add_subplot(2,5,1)
        a2  = fig.add_subplot(2,5,2)
        a3  = fig.add_subplot(2,5,3)
        a4  = fig.add_subplot(2,5,4)
        a5  = fig.add_subplot(2,5,5)
        a6  = fig.add_subplot(2,5,6)
        a7  = fig.add_subplot(2,5,7)
        a8  = fig.add_subplot(2,5,8)
        a9  = fig.add_subplot(2,5,9)
        a10 = fig.add_subplot(2,5,10)

    for i, column in enumerate(df.columns[1:], start=1):

        data_bl_general = df.loc[(df[time] >= last_DRS+CALM_PERIOD_AFTER_TRIG) & (df[time] <= end_bl_1), column]

        data_bl_A = df.loc[(df[time] >= start_bl_A) & (df[time] <= end_bl_A), column]
        data_bl_C = df.loc[(df[time] >= start_bl_C) & (df[time] <= end_bl_C), column]
        data_bl_1 = df.loc[(df[time] >= start_bl_1) & (df[time] <= end_bl_1), column]
        data_bl_2 = df.loc[(df[time] >= start_bl_2) & (df[time] <= end_bl_2), column]
        data_bl_3 = df.loc[(df[time] >= start_bl_3) & (df[time] <= end_bl_3), column]

        data_A = df.loc[(df[time] >= start_A) & (df[time] <= end_A), column]
        data_C = df.loc[(df[time] >= start_C) & (df[time] <= end_C), column]
        data_1 = df.loc[(df[time] >= start_1) & (df[time] <= end_1), column]
        data_2 = df.loc[(df[time] >= start_2) & (df[time] <= end_2), column]
        data_3 = df.loc[(df[time] >= start_3) & (df[time] <= end_3), column]


        # Calculate standard deviation and baseline
        std_dev_A = np.std(data_bl_A)
        std_dev_C = np.std(data_bl_C)
        std_dev_1 = np.std(data_bl_1)
        std_dev_2 = np.std(data_bl_2)
        std_dev_3 = np.std(data_bl_3)

        baseline_A = np.mean(data_bl_A)
        baseline_C = np.mean(data_bl_C)
        baseline_1 = np.mean(data_bl_1)
        baseline_2 = np.mean(data_bl_2)
        baseline_3 = np.mean(data_bl_3)

        # Find the maximum peak amplitude from the calculated baseline
        peak_amplitude_A = np.max(data_A) - baseline_A
        peak_amplitude_C = np.max(data_C) - baseline_C
        peak_amplitude_1 = np.max(data_1) - baseline_1
        peak_amplitude_2 = np.max(data_2) - baseline_2
        peak_amplitude_3 = np.max(data_3) - baseline_3

        stable_baseline = stable_baseline_creteria(data_bl_general)
        accepted_roi = ''

        resp_A = bool(peak_amplitude_A > SIGMAS*std_dev_A)
        resp_C = bool(peak_amplitude_C > SIGMAS*std_dev_C)
        resp_1 = bool(peak_amplitude_1 > SIGMAS*std_dev_1 and peak_amplitude_1 > 0 and i and stable_baseline)
        resp_2 = bool(peak_amplitude_2 > SIGMAS*std_dev_2 and peak_amplitude_2 > 0 and i and stable_baseline)
        resp_3 = bool(peak_amplitude_3 > SIGMAS*std_dev_3 and peak_amplitude_3 > 0 and i and stable_baseline)

        # for debug:
        if DEBUG:
            a1.plot(data_A, color='black', alpha=.5, linewidth=0.5)
            a2.plot(data_C, color='black', alpha=.5, linewidth=0.5)
            a3.plot(data_1, color='black', alpha=.5, linewidth=0.5)
            a4.plot(data_2, color='black', alpha=.5, linewidth=0.5)
            a5.plot(data_3, color='black', alpha=.5, linewidth=0.5)
            a6.plot(data_bl_A, color='black', alpha=.5, linewidth=0.5)
            a7.plot(data_bl_C, color='black', alpha=.5, linewidth=0.5)
            a8.plot(data_bl_1, color='black', alpha=.5, linewidth=0.5)
            a9.plot(data_bl_2, color='black', alpha=.5, linewidth=0.5)
            a10.plot(data_bl_3, color='black', alpha=.5, linewidth=0.5)
        
        bool_resp_1, bool_resp_2, bool_resp_3, ampl_1, ampl_1, ampl_1 = '','','','','',''

        if resp_C and not resp_A:
            # Calculate area under the curve using the trapezoidal rule

            if stable_baseline: accepted_roi = 1           

            if resp_1:
                ampl_1 = np.max(data_1)
                bool_resp_1 = 1
            else:
                ampl_1 = np.nan
                bool_resp_1 = ''

            if resp_2:
                ampl_2 = np.max(data_2)
                bool_resp_2 = 1
            else:
                ampl_2 = np.nan
                bool_resp_2 = ''

            if resp_3:
                ampl_3 = np.max(data_3)
                bool_resp_3 = 1
            else:
                ampl_3 = np.nan
                bool_resp_3 = ''


            auc_1 = np.trapz(data_1, dx=1)
            auc_2 = np.trapz(data_2, dx=1)
            auc_3 = np.trapz(data_3, dx=1)

        else:
            auc_1 = auc_2 = auc_3 = ampl_1 = ampl_2 = ampl_3 = np.nan

        output[i] = [   
                        input,
                        None,
                        std_dev_A,
                        baseline_A,
                        peak_amplitude_A,
                        None,
                        std_dev_C,
                        baseline_C,
                        peak_amplitude_C,
                        None,
                        resp_A if resp_A else None,
                        resp_C if resp_C else None,
                        None,  
                        accepted_roi,                        
                        None,             
                        bool_resp_1,
                        bool_resp_2,
                        bool_resp_3,
                        None,
                        ampl_1,
                        ampl_2,
                        ampl_3,
                        None,
                        auc_1,
                        auc_2,
                        auc_3,
                    ]
    # for debug:
    else:
        if DEBUG:
            plt.show()
            plt.close(fig)

    return output



def main():

    # Initialize result dataframe
    result = pd.DataFrame()

    for line in TODO_LIST_C:
        result = pd.concat([result, process_csv(line[0], **line[1])], axis=1)

    # Add a description column
    result.insert(0, 'Trace: ',
                [
                    'Mice:', 
                    ' ', 
                    'SD A', 
                    'Baseline A', 
                    'Peak Ampl A', 
                    ' ', 
                    'SD C', 
                    'Baseline C', 
                    'Peak Ampl C', 
                    ' ', 
                    'A-responce', 
                    'C-responce', 
                    ' ', 
                    'ROI passes BL stability creteria*',                                         
                    ' ', 
                    'Binary resp. 1',
                    'Binary resp. 2',
                    'Binary resp. 3',
                    ' ', 
                    'Amplitude 1',
                    'Amplitude 2',
                    'Amplitude 3',
                    ' ', 
                    'AUC 1',
                    'AUC 2',
                    'AUC 3',
                ],
            )

    # Save results to a new CSV file
    result.to_csv('C_summary.csv', index=False)


if __name__ == '__main__':
    main()