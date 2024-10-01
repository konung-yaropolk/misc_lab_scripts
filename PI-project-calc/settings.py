#!/usr/bin/env python3
# Settings block:

RESP_DURATION = 2
TO_DO_LIST = [

    ['F:\Lab Work Files\scripts\misc_lab_scripts\PI-project-calc\Field_6_registered.tif',
     {
         'start': 22003,    # in ms
         'movie_duration': 246.167,
         'step_duration': 10,  # in s
         'n_epochs': 10,
         'drs_pattern': [[1, 0],
                         [1, 1]]

     }
     ],

]


if __name__ == '__main__':
    import main
    main.main()
