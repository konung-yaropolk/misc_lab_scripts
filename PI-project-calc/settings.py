#!/usr/bin/env python3
# Settings block:

# Defaults for Derivatives Calculation:
RUN_DERIVATIVES_CALCULATION = False
WORKING_DIR = 'F:/Lab Work Files/2-photon/'
# WORKING_DIR = 'sample/'

STIM_1_NAME = '#1'
STIM_2_NAME = '#2'

RESP_DURATION = 2   # in sec, expected response duration
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


TO_DO_LIST = []


if __name__ == '__main__':
    import classes
    classes.main()
