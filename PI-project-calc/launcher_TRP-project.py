#!/usr/bin/env python3
# Settings block:

# Defaults for Derivatives Calculation:
RUN_DERIVATIVES_CALCULATION = True
WORKING_DIR = 'F:/Lab Work Files/2-photon/'
# WORKING_DIR = 'sample/'

STIM_1_NAME = '#1'
STIM_2_NAME = '#2'

RESP_DURATION = 4  # in sec, expected response duration
STEP_DURATION = 10  # in sec
N_EPOCHS = 1


# Defaults for Derivatives Calculation:
# process all csv files with traces in the WORKING_DIR directory:
RUN_TRACES_CALCULATION = False

RELATIVE_VALUES = True
MEAN_COL_ORDER = 2
COLS_PER_ROI = 4

TIME_BEFORE_TRIG = 10
BASELINE_DURATON = 10
TIME_AFTER_TRIG = None


# TO_DO_LIST - acceptable individual parameters:
# 'drs_pattern'       : [[1, 0, 1, 0, 1, 0],  # stim#1
#                        [0, 1, 0, 0, 1, 0]]  # stim#2
# 'response_duration' : float in sec, expected response duration
# 'output_suffix'     : str
# 'step_duration'     : float in sec
# 'n_epochs'          : int > 0
# 'start_from_epoch'  : int > 0
# 'trig_number'       : int > 0
# 'stim_1_name'       : str
# 'stim_2_name'       : str


TO_DO_LIST = [



    # ['Thy1-RGeco control/2025_08_04_M1/Field_1_Caps_activators_application_ch1_registered_.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '_derivatives_AC',
    #      'n_epochs': 1,
    #      'response_duration': 4,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],

    # ['Thy1-RGeco control/2025_08_04_M2/Field_1_Caps_activators_application_0001_ch1_registered.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '_derivatives_AC',
    #      'n_epochs': 1,
    #      'response_duration': 4,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],


    # ['Thy1-RGeco control/2025_08_04_M3/Field_1_Caps_activators_application_ch1_registered.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '_derivatives_trig1',
    #      'n_epochs': 1,
    #      'response_duration': 4,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],

    # ['Thy1-RGeco control/2025_08_04_M3/Field_1_Caps_activators_application_ch1_registered.tif',
    #  {
    #      'trig_number': 2,
    #      'output_suffix': '_derivatives_trig2',
    #      'n_epochs': 1,
    #      'response_duration': 4,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['Thy1-RGeco control/2025_08_04_M3/Field_1_Caps_activators_application_ch1_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '_derivatives_trig3',
    #      'n_epochs': 1,
    #      'response_duration': 4,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['Thy1-RGeco control/2025_08_04_M3/Field_1_Caps_activators_application_ch1_registered.tif',
    #  {
    #      'trig_number': 4,
    #      'output_suffix': '_derivatives_trig4',
    #      'n_epochs': 1,
    #      'response_duration': 4,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],




]


if __name__ == '__main__':
    import classes
    classes.main(WORKING_DIR,
                 TO_DO_LIST,
                 RUN_DERIVATIVES_CALCULATION,
                 RESP_DURATION,
                 STEP_DURATION,
                 N_EPOCHS,
                 STIM_1_NAME,
                 STIM_2_NAME,
                 RUN_TRACES_CALCULATION,
                 RELATIVE_VALUES,
                 MEAN_COL_ORDER,
                 COLS_PER_ROI,
                 TIME_BEFORE_TRIG,
                 BASELINE_DURATON,
                 TIME_AFTER_TRIG)
