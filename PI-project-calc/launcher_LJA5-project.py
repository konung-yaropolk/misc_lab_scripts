#!/usr/bin/env python3
# Settings block:

# Defaults for Derivatives Calculation:
RUN_DERIVATIVES_CALCULATION = True
WORKING_DIR = 'F:/Lab Work Files/2-photon/'
# WORKING_DIR = 'sample/'

STIM_1_NAME = '#1'
STIM_2_NAME = '#2'

RESP_DURATION = 2  # in sec, expected response duration
STEP_DURATION = 10  # in sec
N_EPOCHS = 1


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


    # #  # Dynorphin applications:


    ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch2_registered.tif',
     {
         'trig_number': 1,
         'output_suffix': 'control',
         'n_epochs': 10,
         'stim_1_name': 'A',
         'stim_2_name': 'C',
         'drs_pattern': [[1, 0],  # stim#1
                         [1, 1]]  # stim#2
     }
     ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 8,
    #      'output_suffix': 'Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch1.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': 'control',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch1.tif',
    #  {
    #      'trig_number': 8,
    #      'output_suffix': 'Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],




    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': 'control',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2.tif',
    #  {
    #      'trig_number': 7,
    #      'output_suffix': 'Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch1.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': 'control',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch1.tif',
    #  {
    #      'trig_number': 7,
    #      'output_suffix': 'Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],








    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_11_Dynorphin_application_ch2.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': 'control',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_11_Dynorphin_application_ch2.tif',
    #  {
    #      'trig_number': 5,
    #      'output_suffix': 'Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_11_Dynorphin_application_ch1.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': 'control',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_11_Dynorphin_application_ch1.tif',
    #  {
    #      'trig_number': 5,
    #      'output_suffix': 'Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],







    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '2s_10hz_control',
    #      'n_epochs': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 10,
    #      'output_suffix': '2s_10hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '0.1Hz_control',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 6,
    #      'output_suffix': '0.1Hz_Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],





    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '_2s_10hz_control',
    #      'n_epochs': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 7,
    #      'output_suffix': '_2s_10hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '_0.1Hz_control',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 8,
    #      'output_suffix': '_0.1Hz_Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],






    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '_2s_10hz_control',
    #      'n_epochs': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 6,
    #      'output_suffix': '_2s_10hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],

    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '_0.1Hz_control',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2_registered.tif',
    #  {
    #      'trig_number': 7,
    #      'output_suffix': '_0.1Hz_Dynorphin_1uM',
    #      'n_epochs': 10,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[1, 0],  # stim#1
    #                      [1, 1]]  # stim#2
    #  }
    #  ],






    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_11_Dynorphin_application_ch1_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '_2s_10hz_control',
    #      'n_epochs': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_11_Dynorphin_application_ch1_registered.tif',
    #  {
    #      'trig_number': 9,
    #      'output_suffix': '_2s_10hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],






    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch1_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '2s_10hz_control',
    #      'n_epochs': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch1_registered.tif',
    #  {
    #      'trig_number': 10,
    #      'output_suffix': '2s_10hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],





    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch1_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '_2s_10hz_control',
    #      'n_epochs': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch1_registered.tif',
    #  {
    #      'trig_number': 7,
    #      'output_suffix': '_2s_10hz_Dynorphin_1uM',
    #      'n_epochs': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],







    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch1_registered.tif',
    #  {
    #      'trig_number': 3,
    #      'output_suffix': '_2s_10hz_control',
    #      'n_epochs': 1,
    #      'stim_1_name': 'A',
    #      'stim_2_name': 'C',
    #      'drs_pattern': [[0],  # stim#1
    #                      [1]]  # stim#2
    #  }
    #  ],
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch1_registered.tif',
    #  {
    #      'trig_number': 6,
    #      'output_suffix': '_2s_10hz_Dynorphin_1uM',
    #      'n_epochs': 1,
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
