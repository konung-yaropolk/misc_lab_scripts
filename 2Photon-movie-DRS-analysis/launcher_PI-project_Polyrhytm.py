#!/usr/bin/env python3
# Default Settings block
# Theese parameters will be used if not specified in the launchers

# Params for Derivatives Calculation:
run_derivatives_calculation = True
working_dir = 'F:/Lab Work Files/2-photon/'


stim_1_name = 'step1'
stim_2_name = 'step2'
output_suffix = '_'
drs_pattern = [[0],  # stim #1
               [1]]  # stim #2

n_epochs = 1
resp_duration = 3   # in sec, expected response duration
step_duration = 10  # in sec


# Params for Traces Calculation:
# process all csv files with traces in the WORKING_DIR directory:
run_traces_calculation = False

relative_values = True
mean_col_order = 2
cols_per_roi = 4

time_before_trig = 10
baseline_duraton = 10
sigmas_treshold = 5
time_after_trig = None

# vertical vertical_shift for all-traces graph in dF/F0 units,
# set 0 to make vertical_shift the same as largest responce
vertical_shift = 1.5

# use vertical shift from this trig to plot in the same scales
vertical_shift_of_trig = 0

# use binarization based on SD from this trig to compare the same ROIs
SD_filter_of_trig = 0

# Use all available CPU cores.
# Faster, but need much more RAM so can be unstable.
multiprocessing = True

# Maximum size of multiprocessing pull
# Set the maximum of processes if there isn't enough RAM
# Set 0 or None to use as many processes as possible
processes_limit = 10


# Params explanation:
#
# 'drs_pattern'       : [[1, 0, 1, 0, 1, 0],  # stim#1
#                        [0, 1, 0, 0, 1, 0]]  # stim#2
# 'resp_duration'     : float in sec, expected response duration
# 'output_suffix'     : str
# 'step_duration'     : float in sec
# 'n_epochs'          : int > 0
# 'start_from_epoch'  : int > 0
# 'trig_number'       : int > 0
# 'stim_1_name'       : str
# 'stim_2_name'       : str


to_do_list = [


    # ######### 2024_04_19 ###################################################

    # ['PI_PP/Homo_A100C_Pre/2024_04_19_Field_1_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_19_Field_2_0001_registered.tif',
    #  {
    #      'n_epochs': 7,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_19_Field_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_19_Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_19_Field_5_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_19_Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],



    # ######### 2024_04_23_ch1 ###################################################

    # ['PI_PP/Homo_A100C_Post/2024_04_23_Field_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_04_23_Field_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_04_23_Field_3_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_04_23_Field_4_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_04_23_Field_5_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_04_23_Field_6_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],



    # ######### 2024_04_23_ch2 ###################################################

    # ['PI_PP/Homo_A100C_Pre/2024_04_23_Field_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_23_Field_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_23_Field_3_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_23_Field_4_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_23_Field_5_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_23_Field_6_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],




    # ######### 2024_04_24_M1 ###################################################

    # ['PI_PP/Homo_A100C_Pre/2024_04_24_M1_Field_1_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_24_M1_Field_2_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_24_M1_Field_3_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],



    # ######### 2024_04_24_M2_ch1 ###################################################

    # ['PI_PP/Homo_A100C_Post/2024_04_24_M2_Field_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_04_24_M2_Field_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 6,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ######### 2024_04_24_M2_ch2 ###################################################

    # ['PI_PP/Homo_A100C_Pre/2024_04_24_M2_Field_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_24_M2_Field_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 6,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],




    # ######### 2024_04_25 ###################################################

    # ['PI_PP/Homo_A100C_Pre/2024_04_25_Field_1_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],




    # ######### 2024_04_29_ch1 ###################################################

    # ['PI_PP/Homo_A100C_Post/2024_04_29_Field_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_04_29_Field_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_04_29_Field_3_enlarged_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_04_29_Field_4_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_04_29_Field_5_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_04_29_Field_6_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_04_29_Field_7_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_04_29_Field_8_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],



    # ######### 2024_04_29_ch2 ###################################################

    # ['PI_PP/Homo_A100C_Pre/2024_04_29_Field_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_29_Field_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_29_Field_3_enlarged_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
    #                      [0, 1, 0, 0, 1, 0]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_29_Field_4_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_29_Field_5_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_29_Field_6_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_29_Field_7_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_04_29_Field_8_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],




    # ######### 2024_05_01_ch1 ###################################################

    # ['PI_PP/Homo_A100C_Post/2024_05_01_Field_1_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_05_01_Field_2_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Post/2024_05_01_Field_3_0001_ch1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],


    # ######### 2024_05_01_ch2 ###################################################

    # ['PI_PP/Homo_A100C_Pre/2024_05_01_Field_1_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_05_01_Field_2_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_PP/Homo_A100C_Pre/2024_05_01_Field_3_0001_ch2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
    #                      [0, 1, 0, 1, 0, 1]]  # stim#2
    #  }
    #  ],




    ########## 2024_11_18_M1_ch1 ###################################################

    ########## 2024_11_18_M1_ch2 ###################################################















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


    # ['Presynaptic inhibition Pirt GCamp3/2024_10_10/Field_14_2_registered.tif',
    #  {
    #      'output_suffix': '_WholeMovie_',
    #      'n_epochs': 28,
    #      'start_from_epoch': 1,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
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
    #      'vertical_shift_of_trig': True,
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

    # ['Presynaptic inhibition Pirt GCamp3/2024_10_11/Field_15_2_registered.tif',
    # {
    # 'output_suffix': '_WholeMovie_',
    # 'n_epochs': 30,
    # 'start_from_epoch': 1,
    # 'drs_pattern': [[1, 0],  # stim#1
    # [1, 1]]  # stim#2
    # }
    # ],
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
    # ['Presynaptic inhibition Pirt GCamp3/2024_10_15/Field_10_registered.tif',
    # {
    # 'output_suffix': '_WholeMovie_',
    # 'n_epochs': 45,
    # 'start_from_epoch': 1,
    # 'drs_pattern': [[1, 0],  # stim#1
    # [1, 1]]  # stim#2
    # }
    # ],
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

    # ['Presynaptic inhibition Pirt GCamp3/2025_02_07/Field_6_DRS+CNQX+AP5_0001_registered.tif',
    # {
    # 'output_suffix': '_WholeMovie_',
    # 'n_epochs': 30,
    # 'start_from_epoch': 1,
    # 'drs_pattern': [[1, 0],  # stim#1
    # [1, 1]]  # stim#2
    # }
    # ],
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
    classes.main(
        working_dir,
        to_do_list,

        run_derivatives_calculation,
        run_traces_calculation,

        resp_duration,
        step_duration,
        n_epochs,
        drs_pattern,

        stim_1_name,
        stim_2_name,

        relative_values,
        mean_col_order,
        cols_per_roi,

        time_before_trig,
        baseline_duraton,
        sigmas_treshold,
        vertical_shift,
        vertical_shift_of_trig,
        SD_filter_of_trig,
        time_after_trig,
    )
