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

    # ['Field_3_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Field_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['Field_3_PI_0001_ch2_registered.tif',
    #  {
    #      'output_suffix': "_JNSKJFBKF_",
    #      'start_from_epoch': 7,
    #      'n_epochs': 4,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],






    # ['Presynaptic inhibition Pirt GCamp3/2024_10_07/Field_2_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_07/Field_3_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/Field_2_0001.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/Field_3.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/Field_5_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/Field_7_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/Field_8_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/Field_9_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/Field_10_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/Field_11_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/Field_12_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/Field_13_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],



    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_5_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_7_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_8_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_9_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_10_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_11_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_12_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_13_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_14_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/Field_15_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],



    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_5_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_7_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_8_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_9_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_10_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_11_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_12_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_13_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_14_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_14_2_registered.tif',
    # #  {
    # #      'output_suffix': '_WholeMovie_',
    # #      'n_epochs': 28,
    # #      'start_from_epoch': 1,
    # #      'drs_pattern': [[1, 0],  # stim#1
    # #                      [1, 1]]  # stim#2
    # #  }
    # #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_14_2_registered.tif',
    #  {
    #      'output_suffix': '_Ctrl_',
    #      'n_epochs': 7,
    #      'start_from_epoch': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_14_2_registered.tif',
    #  {
    #      'output_suffix': '_Bicuculine_20uM_',
    #      'n_epochs': 8,
    #      'start_from_epoch': 20,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],

    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_14_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_15_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_16_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_17_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_18_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],

    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_7_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],



    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_9_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_9_4_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_9_5_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_9_6_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_9_7_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_9_8_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_9_9_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_9_10_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_10_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_10_2_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_10_3_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_10_4_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_10_5_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_10_6_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_10_7_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_10_8_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_10_9_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_11_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_12_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_13_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_14_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_15_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_15_registered.tif',
    #  {
    #      'output_suffix': '_a-stim-single',
    #      'start': 220.504,
    #      'n_epochs': 2,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1],  # stim#1
    #                      [0]]  # stim#2
    #  }
    #  ],

    # # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_15_2_registered.tif',
    # #  {
    # #      'output_suffix': '_WholeMovie_',
    # #      'n_epochs': 30,
    # #      'start_from_epoch': 1,
    # #      'drs_pattern': [[1, 0],  # stim#1
    # #                      [1, 1]]  # stim#2
    # #  }
    # #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_15_2_registered.tif',
    #  {
    #      'output_suffix': '_Ctrl_',
    #      'n_epochs': 10,
    #      'start_from_epoch': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_15_2_registered.tif',
    #  {
    #      'output_suffix': '_Bicuculine_20uM_',
    #      'n_epochs': 10,
    #      'start_from_epoch': 20,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],



    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_15_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_16_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_1_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_4_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_4_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_4_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_4_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_5_0001_registered.tif',
    #  {
    #      'n_epochs': 28,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_7_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_9_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_10_registered.tif',
    # #  {
    # #      'output_suffix': '_WholeMovie_',
    # #      'n_epochs': 45,
    # #      'start_from_epoch': 1,
    # #      'drs_pattern': [[1, 0],  # stim#1
    # #                      [1, 1]]  # stim#2
    # #  }
    # #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_10_registered.tif',
    #  {
    #      'output_suffix': '_Ctrl_',
    #      'n_epochs': 10,
    #      'start_from_epoch': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_10_registered.tif',
    #  {
    #      'output_suffix': '_CNQX_20uM_',
    #      'n_epochs': 10,
    #      'start_from_epoch': 15,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],




    # ['Presynaptic inhibition Pirt GCamp3/2025_02_06/Field_3.tif',
    #  {
    #      'n_epochs': 4,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2025_02_06/Field_4.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2025_02_06/Field_5.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # ['Presynaptic inhibition Pirt GCamp3/2025_02_07/Field_2_DRS_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2025_02_07/Field_4_DRS_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2025_02_07/Field_5_DRS_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],

    # # ['Presynaptic inhibition Pirt GCamp3/2025_02_07/Field_6_DRS+CNQX+AP5_0001_registered.tif',
    # #  {
    # #      'output_suffix': '_WholeMovie_',
    # #      'n_epochs': 30,
    # #      'start_from_epoch': 1,
    # #      'drs_pattern': [[1, 0],  # stim#1
    # #                      [1, 1]]  # stim#2
    # #  }
    # #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2025_02_07/Field_6_DRS+CNQX+AP5_0001_registered.tif',
    #  {
    #      'output_suffix': '_Ctrl_',
    #      'n_epochs': 10,
    #      'start_from_epoch': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3/2025_02_07/Field_6_DRS+CNQX+AP5_0001_registered.tif',
    #  {
    #      'output_suffix': '_CNQX_20uM_AP5_100uM_',
    #      'n_epochs': 10,
    #      'start_from_epoch': 20,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],






















    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_1_galvano.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_2_0001_registered.tif',
    #  {
    #      'n_epochs': 7,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_5_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],





    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/Field_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/Field_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/Field_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/Field_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/Field_3_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/Field_3_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],


    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/Field_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/Field_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/Field_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/Field_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/Field_3_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/Field_3_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M1/Field_1_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M1/Field_2_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M1/Field_3_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M2/Field_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M2/Field_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M2/Field_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 6,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M2/Field_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 6,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_25/Field_1_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_3_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_3_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_3_enlarged_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_3_enlarged_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_4_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_4_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_5_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_5_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_6_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_6_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_7_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_7_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_8_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/Field_8_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_05_01/Field_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_05_01/Field_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_05_01/Field_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_05_01/Field_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_05_01/Field_3_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_05_01/Field_3_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],






    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_1_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_2_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_3_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_4_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_5_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_6_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_7_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_8_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_9_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_10_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_12_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_13_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_14_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_4_PI_0002_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_5_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_6_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_7_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_1_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_2_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_3_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_4_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_5_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_6_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_7_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_8_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_9_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_10_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_10_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_12_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_13_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_14_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_4_PI_0002_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_5_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_6_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],































    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/Field_1_trp_activators_application_ch1_registered_registered_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 16,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/Field_1_trp_activators_application_ch1_registered_registered_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 3,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/Field_1_trp_activators_application_ch2_registered_registered_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 3,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M1/Field_1_trp_activators_application_ch2_registered_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M1/Field_1_trp_activators_application_ch1_registered_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 19,    # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M2/Field_1_trp_activators_application_ch1_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M2/Field_1_trp_activators_application_ch2_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M2/Field_1_DRS_ch1_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_11_trp_activators_application_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_11_trp_activators_application_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_11_DRS_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_8_trp_activators_application_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_8_trp_activators_application_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_9_DRS_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],


































































    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_1_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_1_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_1_3_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_1_4_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_2_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_2_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_3_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_3_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_3_3_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_3_4_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_3_5_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_4_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_4_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_4_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_4_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_4_3_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_4_3_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_4_4_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_4_4_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_5_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_5_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_6_Bradikinin_application_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch1.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],























    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_14/Field_1_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_14/Field_2_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_14/Field_2_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_14/Field_1_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_14/Field_2_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_14/Field_2_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],



    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_14/Field_3_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],

























    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_1_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_1_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_1_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_1_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_1_3_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 3,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_1_3_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 3,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_1_3_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_1_3_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_1_4_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_1_4_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_2_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_2_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_2_3_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_2_4_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

















    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_1_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_1_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_1_3_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_1_4_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_1_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_1_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_1_3_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_1_4_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_2_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_2_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_2_3_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_2_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_2_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_2_3_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_3_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_3_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_4_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_4_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_5_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_5_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_6_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_6_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
















    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_1_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_1_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_1_3_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_1_4_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_1_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_1_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_1_3_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_1_4_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_2_1_0001_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_2_1_0002_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_2_1_0001_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_2_1_0002_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_3_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_3_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_3_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_3_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],



    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_4_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_4_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_4_3_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_4_4_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],



    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_5_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_5_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_5_3_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_5_4_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_6_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_6_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_7_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],



    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_8_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_8_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_8_3_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_8_4_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],



    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_9_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_9_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_9_3_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_9_4_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_9_5_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],



    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_10_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_10_2_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_10_3_Bradikinin_application_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


















    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_1_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_1_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_1_3_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_1_4_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_1_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_1_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_1_3_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_1_4_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],



    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_2_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_2_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_2_3_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_2_4_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_2_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_2_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_2_3_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_2_4_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-A+C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_3_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_3_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_3_3_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_3_4_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_4_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_4_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_4_3_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-C',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_4_4_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-C',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_5_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_5_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_6_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_6_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_7_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L4-A',
    #      'stim_2_name': 'L5-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/Field_7_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'L5-A',
    #      'stim_2_name': 'L4-C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],





















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
                 RESP_DURATION,
                 STEP_DURATION,
                 N_EPOCHS,
                 STIM_1_NAME,
                 STIM_2_NAME,
                 RELATIVE_VALUES,
                 MEAN_COL_ORDER,
                 COLS_PER_ROI,
                 TIME_BEFORE_TRIG,
                 BASELINE_DURATON,
                 TIME_AFTER_TRIG)
