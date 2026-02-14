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
resp_duration = 0.64   # in sec, expected response duration
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
processes_limit = 12


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


    ####### 2024_04_19 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2024_04_19_Field_1_0001_registered.tif',
     {
         'trig_number': 2,
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
                         [0, 1, 0, 0, 1, 0]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_19_Field_2_0001_registered.tif',
     {
         'n_epochs': 7,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
                         [0, 1, 0, 0, 1, 0]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_19_Field_3_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_19_Field_4_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_19_Field_5_registered.tif',
     {
         'n_epochs': 5,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_19_Field_6_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],



    ######### 2024_04_23_ch1 ###################################################

    ['PI_PP/Homo_A100C_C_Post/2024_04_23_Field_1_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
                         [0, 1, 0, 0, 1, 0]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_04_23_Field_2_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
                         [0, 1, 0, 0, 1, 0]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_04_23_Field_3_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
                         [0, 1, 0, 0, 1, 0]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_04_23_Field_4_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_04_23_Field_5_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_04_23_Field_6_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],



    ######### 2024_04_23_ch2 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2024_04_23_Field_1_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
                         [0, 1, 0, 0, 1, 0]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_23_Field_2_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
                         [0, 1, 0, 0, 1, 0]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_23_Field_3_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 1, 0, 1, 0],  # stim#1
                         [0, 1, 0, 0, 1, 0]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_23_Field_4_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_23_Field_5_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_23_Field_6_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],




    ######### 2024_04_24_M1 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2024_04_24_M1_Field_1_0001_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_24_M1_Field_2_0001_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_24_M1_Field_3_0001_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],



    ######### 2024_04_24_M2_ch1 ###################################################

    ['PI_PP/Homo_A100C_C_Post/2024_04_24_M2_Field_1_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_04_24_M2_Field_2_0001_ch1_registered.tif',
     {
         'n_epochs': 6,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],


    ######### 2024_04_24_M2_ch2 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2024_04_24_M2_Field_1_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_24_M2_Field_2_0001_ch2_registered.tif',
     {
         'n_epochs': 6,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],




    ######### 2024_04_25 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2024_04_25_Field_1_0001_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],




    ######### 2024_04_29_ch1 ###################################################

    ['PI_PP/Homo_A100C_C_Post/2024_04_29_Field_1_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_04_29_Field_2_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_04_29_Field_3_enlarged_0001_ch1_registered.tif',
     {
         'n_epochs': 5,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_04_29_Field_4_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_04_29_Field_5_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_04_29_Field_6_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_04_29_Field_7_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_04_29_Field_8_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],



    ######### 2024_04_29_ch2 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2024_04_29_Field_1_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_29_Field_2_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_29_Field_3_enlarged_0001_ch2_registered.tif',
     {
         'n_epochs': 5,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_29_Field_4_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_29_Field_5_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_29_Field_6_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_29_Field_7_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_04_29_Field_8_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],




    ######### 2024_05_01_ch1 ###################################################

    ['PI_PP/Homo_A100C_C_Post/2024_05_01_Field_1_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_05_01_Field_2_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Post/2024_05_01_Field_3_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],


    ######### 2024_05_01_ch2 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2024_05_01_Field_1_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_05_01_Field_2_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_05_01_Field_3_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],




    ######### 2024_11_18_M1_ch1 ###################################################

    ['PI_PP/Homo_Ad100C_C_Post/2024_11_18_M1_Field_1_PI_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad100C_C_Post/2024_11_18_M1_Field_2_PI_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Post/2024_11_18_M1_Field_3_PI_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Post/2024_11_18_M1_Field_4_PI_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Post/2024_11_18_M1_Field_5_PI_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Post/2024_11_18_M1_Field_6_PI_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Post/2024_11_18_M1_Field_7_PI_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Post/2024_11_18_M1_Field_8_PI_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Post/2024_11_18_M1_Field_9_PI_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Post/2024_11_18_M1_Field_10_PI_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],

    ######### 2024_11_18_M1_ch2 ###################################################

    ['PI_PP/Homo_Ad100C_C_Pre/2024_11_18_M1_Field_1_PI_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad100C_C_Pre/2024_11_18_M1_Field_2_PI_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],

    ['PI_PP/Homo_Ad50C_C_Pre/2024_11_18_M1_Field_3_PI_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_11_18_M1_Field_4_PI_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_11_18_M1_Field_5_PI_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_11_18_M1_Field_6_PI_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_11_18_M1_Field_7_PI_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_11_18_M1_Field_8_PI_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_11_18_M1_Field_9_PI_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_11_18_M1_Field_10_PI_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],



    ######### 2024_11_18_M2_ch1 ###################################################

    ['PI_PP/Homo_A50C_C_Post/2024_11_18_M2_Field_4_PI_0002_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A50C_C_Post/2024_11_18_M2_Field_5_PI_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A50C_C_Post/2024_11_18_M2_Field_6_PI_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A50C_C_Post/2024_11_18_M2_Field_7_PI_0001_ch1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],


    ######### 2024_11_18_M2_ch2 ###################################################

    ['PI_PP/Homo_A50C_C_Pre/2024_11_18_M2_Field_4_PI_0002_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A50C_C_Pre/2024_11_18_M2_Field_5_PI_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A50C_C_Pre/2024_11_18_M2_Field_6_PI_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A50C_C_Pre/2024_11_18_M2_Field_7_PI_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],







    ######### 2024_10_07 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2024_10_07_Field_2_0001_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_07_Field_3_0001_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],


    ######### 2024_10_08_M1 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M1_Field_3_0001_ch2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M1_Field_4_0001_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],


    ######### 2024_10_08_M2 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M2_Field_2_0001_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0, 0, 1, 0, 0],  # stim#1
                         [0, 1, 0, 1, 0, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M2_Field_3_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M2_Field_4_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M2_Field_5_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M2_Field_6_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M2_Field_7_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M2_Field_8_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M2_Field_9_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M2_Field_10_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M2_Field_11_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M2_Field_12_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M2_Field_13_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],



    ######### 2024_10_08_M3 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M3_Field_2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M3_Field_3_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M3_Field_4_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M3_Field_5_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M3_Field_6_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M3_Field_7_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M3_Field_8_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M3_Field_9_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M3_Field_11_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M3_Field_12_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M3_Field_13_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M3_Field_14_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_08_M3_Field_15_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],



    ######## 2024_10_10 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_3_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_4_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_5_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_6_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_7_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_8_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_9_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_10_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_11_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_12_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_13_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_10_Field_14_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],

    ['PI_PP/Homo_A100C_C_Pre+Bicuculine/2024_10_10_Field_14_2_registered.tif',
     {
         'trig_number': 1,
         'n_epochs': 6,
         'output_suffix': '_Control',
         'vertical_shift_of_trig': 1,
         'SD_filter_of_trig': 1,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre+Bicuculine/2024_10_10_Field_14_2_registered.tif',
     {
         'trig_number': 1,
         'start_from_epoch': 15,
         'n_epochs': 14,
         'output_suffix': '_Bicuculine_20uM',
         'vertical_shift_of_trig': 1,
         'SD_filter_of_trig': 1,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],



    ######## 2024_10_11 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2024_10_11_Field_1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_11_Field_4_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_11_Field_7_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_11_Field_9_2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_11_Field_10_registered.tif',
     {
         'n_epochs': 5,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad100C_C_Pre/2024_10_11_Field_10_2_registered.tif',
     {
         'n_epochs': 5,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_10_11_Field_10_3_registered.tif',
     {
         'n_epochs': 5,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_11_Field_11_registered.tif',
     {
         'n_epochs': 5,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_11_Field_12_registered.tif',
     {
         'n_epochs': 5,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2024_10_11_Field_13_registered.tif',
     {
         'n_epochs': 5,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad100C_C_Pre/2024_10_11_Field_14_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad100C_C_Pre/2024_10_11_Field_15_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre+Bicuculine/2024_10_11_Field_15_2_registered.tif',
     {
         'trig_number': 1,
         'n_epochs': 12,
         'output_suffix': '_Control',
         'vertical_shift_of_trig': 1,
         'SD_filter_of_trig': 1,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre+Bicuculine/2024_10_11_Field_15_2_registered.tif',
     {
         'trig_number': 1,
         'start_from_epoch': 19,
         'n_epochs': 9,
         'output_suffix': '_Bicuculine_20uM',
         'vertical_shift_of_trig': 1,
         'SD_filter_of_trig': 1,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],


    ####### 2024_10_15 ###################################################

    ['PI_PP/Homo_Ad50C_C_Pre/2024_10_15_Field_1_registered.tif',
     {
         'n_epochs': 5,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_10_15_Field_2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_10_15_Field_3_registered.tif',
     {
         'n_epochs': 10,
         'trig_number': 1,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_10_15_Field_4_1_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_10_15_Field_4_2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_10_15_Field_4_3_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_10_15_Field_4_4_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_10_15_Field_5_0001_registered.tif',
     {
         'n_epochs': 28,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_10_15_Field_6_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad100C_C_Pre/2024_10_15_Field_7_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad100C_C_Pre/2024_10_15_Field_9_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2024_10_15_Field_10_registered.tif',
     {
         'trig_number': 1,
         'n_epochs': 12,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre+CNQX/2024_10_15_Field_10_registered.tif',
     {
         'trig_number': 1,
         'n_epochs': 12,
         'output_suffix': '_Control',
         'vertical_shift_of_trig': 1,
         'SD_filter_of_trig': 1,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre+CNQX/2024_10_15_Field_10_registered.tif',
     {
         'trig_number': 1,
         'start_from_epoch': 21,
         'n_epochs': 16,
         'output_suffix': '_CNQX_20uM',
         'vertical_shift_of_trig': 1,
         'SD_filter_of_trig': 1,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre+CNQX/2024_10_15_Field_10_registered.tif',
     {
         'trig_number': 5,
         'start_from_epoch': 1,
         'n_epochs': 19,
         'output_suffix': '_WO',
         'vertical_shift_of_trig': 1,
         'SD_filter_of_trig': 1,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],


    # ####### 2025_02_06 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2025_02_06_Field_3_0001_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2025_02_06_Field_4_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2025_02_06_Field_5_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],


    ####### 2025_02_07 ###################################################

    ['PI_PP/Homo_A100C_C_Pre/2025_02_07_Field_2_DRS_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A100C_C_Pre/2025_02_07_Field_4_DRS_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A50C_C_Pre/2025_02_07_Field_5_DRS_registered.tif',
     {
         'n_epochs': 5,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre/2025_02_07_Field_6_DRS+CNQX+AP5_0001_registered.tif',
     {
         'trig_number': 1,
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre+CNQX+AP5/2025_02_07_Field_6_DRS+CNQX+AP5_0001_registered.tif',
     {
         'trig_number': 1,
         'n_epochs': 13,
         'output_suffix': '_Control',
         'vertical_shift_of_trig': 1,
         'SD_filter_of_trig': 1,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_Ad50C_C_Pre+CNQX+AP5/2025_02_07_Field_6_DRS+CNQX+AP5_0001_registered.tif',
     {
         'trig_number': 1,
         'start_from_epoch': 20,
         'n_epochs': 11,
         'output_suffix': '_CNQX_20uM_AP5_100uM',
         'vertical_shift_of_trig': 1,
         'SD_filter_of_trig': 1,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],






    ######### 2025_08_22 ###################################################

    ['PI_PP/Homo_A50C_C_Pre/2025_08_22_Field_1_Dynorphin_application_registered.tif',
     {
         'trig_number': 3,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'n_epochs': 10,
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],


    ######### 2025_08_25 ###################################################

    ['PI_PP/Homo_A50C_C_Pre/2025_08_25_Field_1_Dynorphin_application_registered.tif',
     {
         'trig_number': 3,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'n_epochs': 10,
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A50C_C_Pre/2025_08_25_Field_2_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A50C_C_Pre/2025_08_25_Field_3_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['PI_PP/Homo_A50C_C_Pre/2025_08_25_Field_4_registered.tif',
     {
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],


    ######### 2025_08_26 ###################################################

    ['PI_PP/Homo_A50C_C_Pre/2025_08_26_Field_1_registered.tif',
     {
         'trig_number': 3,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'n_epochs': 10,
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],



























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
        multiprocessing,
        processes_limit,
    )
