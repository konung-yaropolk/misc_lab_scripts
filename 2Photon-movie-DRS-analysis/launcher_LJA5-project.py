#!/usr/bin/env python3
# Default Settings block
# Theese parameters will be used if not specified in the launchers

# Params for Derivatives Calculation:
run_derivatives_calculation = True
working_dir = 'F:/Lab Work Files/2-photon/'

stim_1_name = '#1'
stim_2_name = '#2'

resp_duration = 2   # in sec, expected response duration
step_duration = 10  # in sec
n_epochs = 1
drs_pattern = [[0],  # stim #1
               [1]]  # stim #2

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


    # #  # Dynorphin applications:


    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/Field_7_Dynorphin_application_ch2_registered.tif',
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




    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2_registered.tif',
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
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/Field_7_Dynorphin_application_ch2_registered.tif',
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



    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
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
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/Field_7_Dynorphin_application_ch2_registered.tif',
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




    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_11_Dynorphin_application_ch2_registered.tif',
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
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_11_Dynorphin_application_ch2_registered.tif',
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






    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_11_Dynorphin_application_ch2_registered.tif',
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
    # ['PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/Field_11_Dynorphin_application_ch2_registered.tif',
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
        time_after_trig,
    )
