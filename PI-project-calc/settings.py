#!/usr/bin/env python3
# Settings block:

# Defaults:
PATH_PREFIX = 'F:/Lab Work Files/2-photon/'
RESP_DURATION = 2   # in s
STEP_DURATION = 10  # in s
N_EPOCHS = 1


TO_DO_LIST = [


    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_1_galvano_registered.tif',
    #  {
    #      'start': 30434,              # in ms
    #      'movie_duration': 335.638,   # in s
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # A-stim
    #                      [0, 1, 0, 0, 1, 0]]  # C-stim
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_2_0001_registered.tif',
    #  {
    #      'start': 30110,              # in ms
    #      'movie_duration': 448.167,   # in s
    #      'n_epochs': 7,
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # A-stim
    #                      [0, 1, 0, 0, 1, 0]]  # C-stim
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_3_registered.tif',
    #  {
    #      'start': 21978,              # in ms
    #      'movie_duration': 236.167,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_4_registered.tif',
    #  {
    #      'start': 21842,              # in ms
    #      'movie_duration': 249.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_5_registered.tif',
    #  {
    #      'start': 28361,              # in ms
    #      'movie_duration': 158.500,   # in s
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_6_registered.tif',
    #  {
    #      'start': 22003,              # in ms
    #      'movie_duration': 246.167,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],

]


if __name__ == '__main__':
    import main
    main.main()
