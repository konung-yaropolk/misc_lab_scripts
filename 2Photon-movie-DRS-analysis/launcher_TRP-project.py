#!/usr/bin/env python3
# Default Settings block
# Theese parameters will be used if not specified in the launchers

# Params for Derivatives Calculation:
run_derivatives_calculation = True
working_dir = 'F:/Lab Work Files/2-photon/'


stim_1_name = 'A'
stim_2_name = 'C'
drs_pattern = [[0],  # stim #1
               [1]]  # stim #2

n_epochs = 1
resp_duration = 4   # in sec, expected response duration
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

# use vertical shift from this trig to plot in the same scales
vertical_shift_of_trig = 0

# use binarization based on SD from this trig to compare the same ROIs
SD_filter_of_trig = 0


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



    # ['Thy1-RGeco control/2025_08_04_M1/Field_1_Caps_activators_application_ch1_registered_.tif',
    #  {
    #      'trig_number': 1,
    #      'output_suffix': '_derivatives_AC',
    #      'n_epochs': 1,
    #      'response_duration': 4,
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
