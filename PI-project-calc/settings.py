#!/usr/bin/env python3
# Settings block:

# Defaults for Derivatives Calculation:
RUN_DERIVATIVES_CALCULATION = True
WORKING_DIR = 'sample\\'  # 'F: / Lab Work Files/2-photon/'
INPUT_NAME_SUFFIX = '_registered.tif'

RESP_DURATION = 5   # in sec, expected response duration
STEP_DURATION = 10  # in sec
N_EPOCHS = 1


# Defaults for Hyperstack Compositor:
# merge all single channel images into hyperstack in the WORKING_DIR directory:
RUN_HYPERSTACK_COMPOSITOR = True

RED_NAME_ENDING = '_registered.tif_DERIVATIVES_A+C.tif'
GRN_NAME_ENDING = '_registered.tif_DERIVATIVES_C.tif'
BLE_NAME_ENDING = '_registered.tif_DERIVATIVES_A+C.tif'

OUTPUT_NAME_ENDING = '_DERIVATIVES_C-green_A+C-magenta.tif'


# Defaults for Derivatives Calculation:
# process all csv files with traces in the WORKING_DIR directory:
RUN_TRACES_CALCULATION = True

RELATIVE_VALUES = True
MEAN_COL_ORDER = 2
COLS_PER_ROI = 4

TIME_BEFORE_TRIG = 10
BASELINE_DURATON = 10
TIME_AFTER_TRIG = None


# TO_DO_LIST - acceptable individual parameters:
# 'drs_pattern'       : [[1, 0, 1, 0, 1, 0],  # A-stim
#                        [0, 1, 0, 0, 1, 0]]  # C-stim
# 'response_duration' : float in sec, expected response duration
# 'filename_suffix'   : str
# 'step_duration'     : float in sec
# 'n_epochs'          : int
# 'trig_number'       : int

TO_DO_LIST = [

    ['Field_6_registered.tif',
     {
         'n_epochs': 10,
         'drs_pattern': [[1, 0],  # A-stim
                         [1, 1]]  # C-stim
     }
     ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_1_galvano_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # A-stim
    #                      [0, 1, 0, 0, 1, 0]]  # C-stim
    #  }
    # ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_2_0001_registered.tif',
    #  {
    #      'n_epochs': 7,
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # A-stim
    #                      [0, 1, 0, 0, 1, 0]]  # C-stim
    #  }
    # ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    # ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    # ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_5_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    # ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    # ],



    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_2_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # A-stim
    #                      [0, 1, 0, 1, 0, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_5_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_7_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_8_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_9_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_10_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_11_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_12_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_13_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],



    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_5_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_7_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_8_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_9_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_10_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_11_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_12_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_13_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_14_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_15_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],



    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_5_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_7_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_8_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_9_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_10_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_11_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_12_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_13_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_14_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_14_2_registered.tif',
    #  {
    #      'n_epochs': 30,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_14_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_15_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_16_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_17_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_18_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],

    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_7_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],



    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_4_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_5_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_6_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_7_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_8_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_9_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_10_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_2_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_3_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_4_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_5_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_6_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_7_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_8_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_9_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_11_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_12_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_13_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_14_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_15_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_15_registered.tif',
    #  {
    #      'start': 220.504,
    #      'n_epochs': 2,
    #      'drs_pattern': [[1],  # A-stim
    #                      [0]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_15_2_registered.tif',
    #  {
    #      'n_epochs': 30,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_15_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_16_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],




    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_1_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_2_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_3_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_4_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_5_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_6_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_7_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_8_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_9_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_10_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_12_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_13_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_14_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_4_PI_0002_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_5_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_6_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_7_PI_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_1_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_2_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_3_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_4_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_5_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_6_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_7_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_8_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_9_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_10_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_12_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_13_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_14_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_4_PI_0002_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_5_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_6_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_7_PI_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],


















































    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/Field_1_trp_activators_application_ch1_registered_registered_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 16,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/Field_1_trp_activators_application_ch1_registered_registered_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 3,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/Field_1_trp_activators_application_ch2_registered_registered_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 3,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M1/Field_1_trp_activators_application_ch2_registered_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M1/Field_1_trp_activators_application_ch1_registered_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 19,    # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M2/Field_1_trp_activators_application_ch1_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M2/Field_1_trp_activators_application_ch2_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M2/Field_1_DRS_ch1_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_11_trp_activators_application_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_11_trp_activators_application_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/Field_11_DRS_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],



    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_8_trp_activators_application_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_8_trp_activators_application_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],
    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/Field_9_DRS_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 1,
    #      'trig_number': 2,     # number of trigger, starting from 1
    #      'drs_pattern': [[0],  # A-stim
    #                      [1]]  # C-stim
    #  }
    #  ],


]


if __name__ == '__main__':
    import classes
    classes.main()
