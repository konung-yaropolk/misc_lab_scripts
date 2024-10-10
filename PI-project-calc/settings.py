#!/usr/bin/env python3
# Settings block:

# Defaults:
PATH_PREFIX = 'F:/Lab Work Files/2-photon/'
RESP_DURATION = 1   # in s
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



    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M2/Field_2_0001_registered.tif',
    #  {
    #      'start': 20939,              # in ms
    #      'movie_duration': 633.167,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # A-stim
    #                      [0, 1, 0, 1, 0, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M2/Field_3_registered.tif',
    #  {
    #      'start': 20574,              # in ms
    #      'movie_duration': 231.167,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M2/Field_4_registered.tif',
    #  {
    #      'start': 20653,              # in ms
    #      'movie_duration': 228.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M2/Field_5_registered.tif',
    #  {
    #      'start': 20780,              # in ms
    #      'movie_duration': 269.667,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M2/Field_6_registered.tif',
    #  {
    #      'start': 20804,              # in ms
    #      'movie_duration': 236.000,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M2/Field_7_registered.tif',
    #  {
    #      'start': 20839,              # in ms
    #      'movie_duration': 248.333,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M2/Field_8_registered.tif',
    #  {
    #      'start': 20920,              # in ms
    #      'movie_duration': 225.667,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M2/Field_9_registered.tif',
    #  {
    #      'start': 20839,              # in ms
    #      'movie_duration': 248.333,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M2/Field_10_registered.tif',
    #  {
    #      'start': 20989,              # in ms
    #      'movie_duration': 254.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M2/Field_11_registered.tif',
    #  {
    #      'start': 20783,              # in ms
    #      'movie_duration': 245.000,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M2/Field_12_registered.tif',
    #  {
    #      'start': 20914,              # in ms
    #      'movie_duration': 245.500,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M2/Field_13_registered.tif',
    #  {
    #      'start': 23072,              # in ms
    #      'movie_duration': 257.000,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],

    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_2_registered.tif',
    #  {
    #      'start': 20946,              # in ms
    #      'movie_duration': 244.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_3_registered.tif',
    #  {
    #      'start': 20796,              # in ms
    #      'movie_duration': 250.000,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_4_registered.tif',
    #  {
    #      'start': 20824,              # in ms
    #      'movie_duration': 249.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_5_registered.tif',
    #  {
    #      'start': 20546,              # in ms
    #      'movie_duration': 249.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_6_registered.tif',
    #  {
    #      'start': 20468,              # in ms
    #      'movie_duration': 249.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_7_registered.tif',
    #  {
    #      'start': 20828,              # in ms
    #      'movie_duration': 249.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_8_registered.tif',
    #  {
    #      'start': 20708,              # in ms
    #      'movie_duration': 249.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_9_registered.tif',
    #  {
    #      'start': 20923,              # in ms
    #      'movie_duration': 249.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_10_registered.tif',
    #  {
    #      'start': 20346,              # in ms
    #      'movie_duration': 249.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_11_registered.tif',
    #  {
    #      'start': 20637,              # in ms
    #      'movie_duration': 249.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_12_registered.tif',
    #  {
    #      'start': 20984,              # in ms
    #      'movie_duration': 249.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_13_registered.tif',
    #  {
    #      'start': 20702,              # in ms
    #      'movie_duration': 249.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_14_registered.tif',
    #  {
    #      'start': 31338,              # in ms
    #      'movie_duration': 249.833,   # in s
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    ['GCamp3+jRgeco_injection + DRS + Caps/2024_10_08_M3/Field_15_registered.tif',
     {
         'start': 24278,              # in ms
         'movie_duration': 249.833,   # in s
         'n_epochs': 10,
         'drs_pattern': [[1, 0],  # A-stim
                         [1, 1]]  # C-stim
     }
     ],



]


if __name__ == '__main__':
    import main
    main.main()

# %%
