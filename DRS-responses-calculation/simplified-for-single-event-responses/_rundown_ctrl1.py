import classes
import os

# output:
OUTPUT_CSV = 'summary_rundown_ctrl1.csv'

# analysis params:
SIGMAS = 5                    # number of sdandard deviation as signal threshold
BASELINE_TRESHOLD = 0.5         # maximum amplitude of baseline deviation for ROI to be accepted (in dF/F0)

# timings:
CALM_PERIOD = 10              # time in sec before trigger for baseline


# debug mode
DEBUG = False
SAVE_SELECTED = False


# triggers time value in ms:
TODO_LIST_C = [ 

['_rundown_ctrl1_mouse_1',
    {
    'stim_A' : 0,
    'stim_C' : 0,
    },],

   
]




def main():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    output = os.path.join(script_dir, OUTPUT_CSV)

    classes.Calc(TODO_LIST_C,
            output,
            SIGMAS,
            BASELINE_TRESHOLD,
            CALM_PERIOD,
            DEBUG,
            SAVE_SELECTED)

if __name__ == '__main__':
    main()
