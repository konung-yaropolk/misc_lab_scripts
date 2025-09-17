#!/usr/bin/env python3
# Default Settings block
# Theese parameters will be used if not specified in the launchers

# Params for Derivatives Calculation:
run_derivatives_calculation = False
working_dir = 'F:/Lab Work Files/2-photon/'


stim_1_name = 'A'
stim_2_name = 'C'
drs_pattern = [[0],  # stim #1
               [1]]  # stim #2

n_epochs = 1
resp_duration = 3   # in sec, expected response duration
step_duration = 10  # in sec


# Params for Traces Calculation:
# process all csv files with traces in the WORKING_DIR directory:
run_traces_calculation = True

relative_values = True
mean_col_order = 2
cols_per_roi = 4

time_before_trig = 10
baseline_duraton = 10
sigmas_treshold = 5
time_after_trig = None

# vertical vertical_shift for all-traces graph in dF/F0 units,
# set 0 to make vertical_shift the same as largest responce
vertical_shift = 0

# use vertical shift from previous run to plot in the same scales
use_last_vertical_shift = False

# use binarixation based on SD from previous run to compare the same ROIs
use_last_SD_filter = False

# Use all available CPU cores.
# Faster, but need much more RAM so can be unstable.
multiprocessing = True

# Maximum size of multiprocessing pull
# Set the maximum of processes if there isn't enough RAM
# Set 0 or None to use as many processes as possible
processes_limit = 14


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





    # ['LJA5 project CNO Dynorphin and PI DRS Polyrythm/2025_09_12/Test.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '_test_0hour',
    #      'n_epochs': 1,
    #      'use_last_vertical_shift': False,
    #      'use_last_SD_filter': False,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # ['LJA5 project CNO Dynorphin and PI DRS Polyrythm/2025_09_12/Test.tif',
    #  {
    #      'trig_number': 2,
    #      'output_suffix': '_test_1hour',
    #      'n_epochs': 1,
    #      'use_last_vertical_shift': False,
    #      'use_last_SD_filter': False,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],









    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '2s_10hz_control',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 10,
    #      'output_suffix': '2s_10hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '0.1Hz_control',
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 6,
    #      'output_suffix': '0.1Hz_Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],





    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '_2s_10hz_control',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 7,
    #      'output_suffix': '_2s_10hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '_0.1Hz_control',
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 8,
    #      'output_suffix': '_0.1Hz_Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],






    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '_2s_10hz_control',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 6,
    #      'output_suffix': '_2s_10hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '_0.1Hz_control',
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 7,
    #      'output_suffix': '_0.1Hz_Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],






    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_11_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '_2s_10hz_control',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_11_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 9,
    #      'output_suffix': '_2s_10hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],






    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch1_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '2s_10hz_control',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch1_registered.tif',
    #  {
    #      'trig_number': 10,
    #      'output_suffix': '2s_10hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],







    # # Dynorphin applications:


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': 'control',
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 8,
    #      'output_suffix': 'Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'use_last_vertical_shift': True,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],




    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': 'control',
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 7,
    #      'output_suffix': 'Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'use_last_vertical_shift': True,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],






















































    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '0.1Hz_control',
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 7,
    #      'output_suffix': '0.1Hz_Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'use_last_vertical_shift': True,
    #      'use_last_SD_filter': True,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '10Hz_control',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 5,
    #      'output_suffix': '10Hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'use_last_vertical_shift': True,
    #      'use_last_SD_filter': True,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],







    # ['LJA5 project Dynorphin control/2025_08_22/Field_1_Dynorphin_application_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '0.1Hz_control',
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['LJA5 project Dynorphin control/2025_08_22/Field_1_Dynorphin_application_registered.tif',
    #  {
    #      'trig_number': 5,
    #      'output_suffix': '0.1Hz_Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'use_last_vertical_shift': True,
    #      'use_last_SD_filter': True,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['LJA5 project Dynorphin control/2025_08_22/Field_1_Dynorphin_application_registered.tif',
    #  {
    #      'trig_number': 2,
    #      'output_suffix': '2Hz_control',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['LJA5 project Dynorphin control/2025_08_22/Field_1_Dynorphin_application_registered.tif',
    #  {
    #      'trig_number': 6,
    #      'output_suffix': '2Hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'use_last_vertical_shift': True,
    #      'use_last_SD_filter': True,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['LJA5 project Dynorphin control/2025_08_22/Field_1_Dynorphin_application_registered.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '10Hz_control',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['LJA5 project Dynorphin control/2025_08_22/Field_1_Dynorphin_application_registered.tif',
    #  {
    #      'trig_number': 7,
    #      'output_suffix': '10Hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'use_last_vertical_shift': True,
    #      'use_last_SD_filter': True,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],



    # ['LJA5 project Dynorphin control/2025_08_25/Field_1_Dynorphin_application_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '0.1Hz_control',
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['LJA5 project Dynorphin control/2025_08_25/Field_1_Dynorphin_application_registered.tif',
    #  {
    #      'trig_number': 5,
    #      'output_suffix': '0.1Hz_Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'use_last_vertical_shift': True,
    #      'use_last_SD_filter': True,
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['LJA5 project Dynorphin control/2025_08_25/Field_1_Dynorphin_application_registered.tif',
    #  {
    #      'trig_number': 2,
    #      'output_suffix': '2Hz_control',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['LJA5 project Dynorphin control/2025_08_25/Field_1_Dynorphin_application_registered.tif',
    #  {
    #      'trig_number': 6,
    #      'output_suffix': '2Hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'use_last_vertical_shift': True,
    #      'use_last_SD_filter': True,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['LJA5 project Dynorphin control/2025_08_25/Field_1_Dynorphin_application_registered.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '10Hz_control',
    #      'n_epochs': 1,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['LJA5 project Dynorphin control/2025_08_25/Field_1_Dynorphin_application_registered.tif',
    #  {
    #      'trig_number': 7,
    #      'output_suffix': '10Hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'use_last_vertical_shift': True,
    #      'use_last_SD_filter': True,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['LJA5 project Dynorphin control/2025_08_25/Field_1_Dynorphin_application_registered.tif',
    #  {
    #      'trig_number': 9,
    #      'output_suffix': '10Hz_Naloxone_5uM',
    #      'n_epochs': 1,
    #      'use_last_vertical_shift': True,
    #      'use_last_SD_filter': True,
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],


    ['LJA5 project Dynorphin control/2025_08_26/Field_1_registered.tif',
     {
         'trig_number': 3,
         'output_suffix': '0.1Hz_control',
         'n_epochs': 10,
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['LJA5 project Dynorphin control/2025_08_26/Field_1_registered.tif',
     {
         'trig_number': 5,
         'output_suffix': '0.1Hz_Dynorphin_1uM',
         'n_epochs': 10,
         'use_last_vertical_shift': True,
         'use_last_SD_filter': True,
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    ['LJA5 project Dynorphin control/2025_08_26/Field_1_registered.tif',
     {
         'trig_number': 11,
         'output_suffix': '0.1Hz_Naloxone_5uM',
         'n_epochs': 10,
         'use_last_vertical_shift': True,
         'use_last_SD_filter': True,
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],


    ['LJA5 project Dynorphin control/2025_08_26/Field_1_registered.tif',
     {
         'trig_number': 2,
         'output_suffix': '2Hz_control',
         'n_epochs': 1,
         'drs_pattern': [[0],  # stim#1
                         [1]]  # stim#2
     }
     ],
    ['LJA5 project Dynorphin control/2025_08_26/Field_1_registered.tif',
     {
         'trig_number': 6,
         'output_suffix': '2Hz_Dynorphin_1uM',
         'n_epochs': 1,
         'use_last_vertical_shift': True,
         'use_last_SD_filter': True,
         'drs_pattern': [[0],  # stim#1
                         [1]]  # stim#2
     }
     ],
    ['LJA5 project Dynorphin control/2025_08_26/Field_1_registered.tif',
     {
         'trig_number': 10,
         'output_suffix': '2Hz_Naloxone_5uM',
         'n_epochs': 1,
         'use_last_vertical_shift': True,
         'use_last_SD_filter': True,
         'drs_pattern': [[0],  # stim#1
                         [1]]  # stim#2
     }
     ],

    ['LJA5 project Dynorphin control/2025_08_26/Field_1_registered.tif',
     {
         'trig_number': 1,
         'output_suffix': '10Hz_control',
         'n_epochs': 1,
         'drs_pattern': [[0],  # stim#1
                         [1]]  # stim#2
     }
     ],
    ['LJA5 project Dynorphin control/2025_08_26/Field_1_registered.tif',
     {
         'trig_number': 7,
         'output_suffix': '10Hz_Dynorphin_1uM',
         'n_epochs': 1,
         'use_last_vertical_shift': True,
         'use_last_SD_filter': True,
         'drs_pattern': [[0],  # stim#1
                         [1]]  # stim#2
     }
     ],
    ['LJA5 project Dynorphin control/2025_08_26/Field_1_registered.tif',
     {
         'trig_number': 9,
         'output_suffix': '10Hz_Naloxone_5uM',
         'n_epochs': 1,
         'use_last_vertical_shift': True,
         'use_last_SD_filter': True,
         'drs_pattern': [[0],  # stim#1
                         [1]]  # stim#2
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
        use_last_vertical_shift,
        use_last_SD_filter,
        time_after_trig,
        multiprocessing,
        processes_limit,
    )
