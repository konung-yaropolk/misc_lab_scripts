import classes
import os

# output:
OUTPUT_CSV = 'summary_DRS_Neurons.csv'

# analysis params:
SIGMAS = 5                    # number of sdandard deviation as signal threshold
                              # maximum amplitude of baseline deviation for ROI to be accepted (in dF/F0)
BASELINE_TRESHOLD = 0.5

# timings:
CALM_PERIOD = 10              # time in sec before trigger for baseline
CALM_PERIOD_AFTER_TRIG = 20   # time in sec after trigger for baseline
SKIP_AFTER_APPLICATION = 60   # time to skip in sec after application started

# if False - return boutons (not considered as fibers)
YEILD_FIBERS = False

# debug mode
DEBUG = False
SAVE_SELECTED = False


# triggers time value in ms:
TODO_LIST_C = [

    ['2024_04_24_M2_N',
     {
         'stim_A': 59928,
         'stim_C': 155625,
         'stim_AC': 105681,
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
                 CALM_PERIOD_AFTER_TRIG,
                 SKIP_AFTER_APPLICATION,
                 YEILD_FIBERS,
                 DEBUG,
                 SAVE_SELECTED)


if __name__ == '__main__':
    main()
