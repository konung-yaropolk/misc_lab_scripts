import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# analysis params:
SIGMAS = 5                    # number of sdandard deviation as signal threshold
BASELINE_TRESHOLD = 0.5         # maximum amplitude of baseline deviation for ROI to be accepted (in dF/F0)

# timings:
CALM_PERIOD = 10              # time in sec before trigger for baseline
CALM_PERIOD_AFTER_TRIG = 20   # time in sec after trigger for baseline
SKIP_AFTER_APPLICATION = 60   # time to skip in sec after application started

YEILD_FIBERS = False          # if False - return boutons (not considered as fibers)

# debug mode
DEBUG = False
SAVE_SELECTED = True


# triggers time value in ms:
TODO_LIST_C = [ 

['2024_04_29_N',
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

]

def stable_baseline_creteria(baseline):
    
    # Apply Gaussian smoothing
    # sigma = SIGMAS  # Standard deviation for Gaussian kernel
    smoothed_baseline = gaussian_filter1d(baseline, 1)
    amplitude = smoothed_baseline.max() - smoothed_baseline.min()
    decision = amplitude < BASELINE_TRESHOLD
    
    # if not decision:
    #     plt.figure(figsize=(10, 6))
    #     plt.plot(baseline, label='Original Noisy Sequence')
    #     plt.plot(smoothed_baseline, label='Smoothed Sequence', linewidth=2)
    #     plt.legend()
    #     plt.grid(True)
    #     plt.savefig('unstable_rois_Neurons/{}.jpg'.format(np.random.randint(10000)))
    #     plt.close()

    return decision


def process_csv(input, stim_A, stim_C, appl_1, wout_1, appl_2, wout_2, appl_3, fibers, last_DRS=None):

    # Define time ranges
    start_bl_A, end_bl_A   = -CALM_PERIOD+stim_A/1000, -1+stim_A/1000
    start_A, end_A         = -4 +stim_A/1000,  5 +stim_A/1000 

    start_bl_C, end_bl_C   = -CALM_PERIOD+stim_C/1000, -1+stim_C/1000
    start_C, end_C         = -4 +stim_C/1000,  5 +stim_C/1000

    last_DRS = last_DRS/1000 if last_DRS else end_C

    start_bl_1, end_bl_1   = -CALM_PERIOD+appl_1/1000, CALM_PERIOD_AFTER_TRIG+appl_1/1000
    start_1, end_1 = SKIP_AFTER_APPLICATION+appl_1/1000,    wout_1/1000

    start_bl_2, end_bl_2   = -CALM_PERIOD+appl_2/1000, CALM_PERIOD_AFTER_TRIG+appl_2/1000
    start_2, end_2 = SKIP_AFTER_APPLICATION+appl_2/1000,    wout_2/1000

    start_bl_3, end_bl_3   = -CALM_PERIOD+appl_3/1000, CALM_PERIOD_AFTER_TRIG+appl_3/1000
    start_3, end_3 = SKIP_AFTER_APPLICATION+appl_3/1000, 100000

    # Load the data
    df = pd.read_csv(input + '.csv')
    output = pd.DataFrame()

    accepted_roi_list = []

    # make zero timepoint at the beginning
    time = df.columns[0]
    df[time] = df[time] - df[time].iloc[0] + (df[time].iloc[1] - df[time].iloc[0])

    # find dx for integration - time resolution (in 1/fps)
    dt = abs(df[time].iloc[1] - df[time].iloc[2])

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
        std_dev_bl_general = np.std(data_bl_general)
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

        resp_A = True #peak_amplitude_A > SIGMAS*std_dev_A
        resp_C = True #peak_amplitude_C > SIGMAS*std_dev_C
        resp_1 = peak_amplitude_1 > SIGMAS*std_dev_bl_general and peak_amplitude_1 > 0 and ((i in fibers) == YEILD_FIBERS) and stable_baseline
        resp_2 = peak_amplitude_2 > SIGMAS*std_dev_bl_general and peak_amplitude_2 > 0 and ((i in fibers) == YEILD_FIBERS) and stable_baseline
        resp_3 = peak_amplitude_3 > SIGMAS*std_dev_bl_general and peak_amplitude_3 > 0 and ((i in fibers) == YEILD_FIBERS) and stable_baseline
        #print(SIGMAS*std_dev_bl_general)

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
        
        bool_resp_1, bool_resp_2, bool_resp_3, ampl_1, ampl_2, ampl_3, ampl_1_all, ampl_2_all, ampl_3_all, set_1, set_2, set_3, intersection_1_2, intersection_2_3, intersection_1_3, intersection_1_2_3 = '','','','','','','','','','','','','','','',''

        if ((i in fibers) == YEILD_FIBERS):
            # Calculate area under the curve using the trapezoidal rule

            if stable_baseline: 
                accepted_roi = 1
                accepted_roi_list.append(i)

                ampl_1_all = peak_amplitude_1
                ampl_2_all = peak_amplitude_2
                ampl_3_all = peak_amplitude_3

            if resp_1:
                ampl_1 = peak_amplitude_1
                bool_resp_1 = 1
                auc_1 = np.trapz(data_1, dx=dt)
            else:
                ampl_1 = np.nan
                auc_1 = np.nan
                bool_resp_1 = ''

            if resp_2:
                ampl_2 = peak_amplitude_2
                bool_resp_2 = 1
                auc_2 = np.trapz(data_2, dx=dt)
            else:
                ampl_2 = np.nan
                auc_2 = np.nan
                bool_resp_2 = ''

            if resp_3:
                ampl_3 = peak_amplitude_3
                bool_resp_3 = 1
                auc_3 = np.trapz(data_3, dx=dt)
            else:
                ampl_3 = np.nan
                auc_3 = np.nan
                bool_resp_3 = ''

            if bool_resp_1 and not bool_resp_2 and not bool_resp_3: set_1 = 1
            if bool_resp_2 and not bool_resp_1 and not bool_resp_3: set_2 = 1
            if bool_resp_3 and not bool_resp_2 and not bool_resp_1: set_3 = 1
            if bool_resp_1 and bool_resp_2 and not bool_resp_3: intersection_1_2 = 1
            if bool_resp_1 and bool_resp_3 and not bool_resp_2: intersection_1_3 = 1
            if bool_resp_2 and bool_resp_3 and not bool_resp_1: intersection_2_3 = 1
            if bool_resp_1 and bool_resp_2 and bool_resp_3: intersection_1_2_3 = 1

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
                        set_1,
                        set_2,
                        set_3,
                        intersection_1_2,
                        intersection_1_3,
                        intersection_2_3,
                        intersection_1_2_3,                                           
                        None,
                        ampl_1,
                        ampl_2,
                        ampl_3,
                        None,
                        ampl_1_all,
                        ampl_2_all,
                        ampl_3_all,
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

        if SAVE_SELECTED:
            # Create a new DataFrame with only the first column and needed columns
            selected_columns = [df.columns[0]] + [df.columns[i] for i in accepted_roi_list]
            new_df = df[selected_columns]

            # Write the new DataFrame to a CSV file
            new_df.to_csv(input + '_selected_ROI_boutons.csv', index=False)

            # with open(input + '_selected_ROI_list.txt', 'w') as output:
            #     output.write(str(accepted_roi_list))
            print(accepted_roi_list)

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
                    'set_1',
                    'set_2',
                    'set_3',                    
                    'intersection_1_2',
                    'intersection_1_3',
                    'intersection_2_3',
                    'intersection_1_2_3',         
                    ' ', 
                    'Amplitude 1',
                    'Amplitude 2',
                    'Amplitude 3',
                    ' ', 
                    'Amplitude 1 all',
                    'Amplitude 2 all',
                    'Amplitude 3 all',
                    ' ', 
                    'AUC 1',
                    'AUC 2',
                    'AUC 3',
                ],
            )

    # Save results to a new CSV file
    result.to_csv('summary_Neurons.csv', index=False)


if __name__ == '__main__':
    main()
