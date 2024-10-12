#!/usr/bin/env python3
# Settings block:

# Defaults:
PATH_PREFIX = 'F:/Lab Work Files/2-photon/'
INPUT_NAME_SUFFIX = '_registered.tif'

RESP_DURATION = 1   # in s
STEP_DURATION = 10  # in s
N_EPOCHS = 1


RED_NAME_ENDING = '_registered.tif_DERIVATIVES_A+C.tif'
GRN_NAME_ENDING = '_registered.tif_DERIVATIVES_C.tif'
BLE_NAME_ENDING = '_registered.tif_DERIVATIVES_A+C.tif'

OUTPUT_NAME_ENDING = '_DERIVATIVES_C-green_A+C-red.tif'


TO_DO_LIST = [


    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_1_galvano_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # A-stim
    #                      [0, 1, 0, 0, 1, 0]]  # C-stim
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_2_0001_registered.tif',
    #  {
    #      'n_epochs': 7,
    #      'drs_pattern': [[1, 0, 1, 0, 1, 0],  # A-stim
    #                      [0, 1, 0, 0, 1, 0]]  # C-stim
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_5_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],

    # ['TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],



    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_2_0001_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0, 0, 1, 0, 0],  # A-stim
    #                      [0, 1, 0, 1, 0, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_5_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_7_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_8_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_9_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_10_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_11_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_12_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M2/Field_13_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],

    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_5_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_7_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_8_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_9_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_10_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_11_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_12_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_13_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_14_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_08_M3/Field_15_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],


    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_5_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_6_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_7_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_8_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_9_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_10_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_11_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_12_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_13_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_14_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_14_2_registered.tif',
    #  {
    #      'n_epochs': 30,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_14_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_15_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_16_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_17_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_10/Field_18_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],


    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_1_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_4_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_7_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],

    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_2_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_4_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_5_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_6_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_7_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_8_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_9_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_9_10_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_2_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_3_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_4_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_5_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_6_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_7_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_8_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_10_9_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_11_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_12_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_13_registered.tif',
    #  {
    #      'n_epochs': 5,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_14_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_15_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],

    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_15_2_registered.tif',
    #  {
    #      'n_epochs': 30,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_15_3_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],
    # ['Presynaptic inhibition Pirt GCamp3 + Bicuculine/2024_10_11/Field_16_registered.tif',
    #  {
    #      'n_epochs': 10,
    #      'drs_pattern': [[1, 0],  # A-stim
    #                      [1, 1]]  # C-stim
    #  }
    #  ],




]


if __name__ == '__main__':
    import main
    main.main()
