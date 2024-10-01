#!/usr/bin/env python3
# Settings block:

# Defaults:
RESP_DURATION = 2   # in s
STEP_DURATION = 10  # in s
N_EPOCHS = 1


TO_DO_LIST = [

    ['F:\Lab Work Files\scripts\misc_lab_scripts\PI-project-calc\Field_6_registered.tif',
     {
         'start': 22003,    # in ms
         'movie_duration': 246.167,
         'n_epochs': 10,
         'drs_pattern': [[1, 0],  # A-stim
                         [1, 1]]  # C-stim
     }
     ],

]


if __name__ == '__main__':
    import main
    main.main()
