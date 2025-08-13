#!/usr/bin/env python3
# Settings block:


DIRECTORY = 'data/'
# Provide full path to files. Leave quotes empty if the files in the same directory with this script

DISTORTION_TYPE = 'BILINEAR'
# TRANSLATION        - translation
# RIGID_BODY         - translation + rotation
# SCALED_ROTATION    - translation + rotation + scaling
# AFFINE             - translation + rotation + scaling + shearing
# BILINEAR           - non-linear transformation (no support for 'previous' reference frame mode)

REFERENCE_FRAME = 'first'
# first, previous, mean

NUMBER_OF_REF_FRAMES = 15
# If reference is 'first', then this parameter specifies the
# number of frames from the beginning of the stack that
# should be averaged to yield the reference image.

MOVING_AVERAGE = 15
# If moving_average is greater than 1, a moving average of
# the stack is first created (using a subset size of
# moving_average) before registration

REFERENCE_CHANNEL = 0
# what channel use as refferense, 0 - use mean of all

TIME_AXIS = 0
# The axis of the time dimension in original TIFF array (default 0)

SPLIT_ONLY = False
# Just simple split stack by channels with no registration. Set True or False

TAKE_ALL_FILES = False
# Process all .tif files recurcively in given directory
# If this parameter turned on, TODO_LIST will be ignored

SAVE_TRANSFORM_MATRIX = True
# Save transform matrix in .npy file with the same filename as original .tif

READ_TRANSFORM_MATRIX = False
# Read transform matrix from .npy file with the same filename as original .tif

MULTIPROCESSING = False
# Use all available CPU cores.
# Faster, but need much more RAM so can be unstable.

PROCESSES_LIMIT = 10
# Maximum size of multiprocessing pull
# Set the maximum of processes if there isn't enough RAM
# Set 0 or None to use as many processes as possible


TODO_LIST = [                   # list here quoted TIFF file names without .tiff extensions, separated by comma:



    # # TRP project

    # ['Field 1_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2023_12_22_M1/',
    #     'DISTORTION_TYPE' : 'TRANSLATION',
    #     'REFERENCE_FRAME' : 'previous',
    #     'REFERENCE_CHANNEL' : 1,
    #     'NUMBER_OF_REF_FRAMES' : 1,
    #     'MOVING_AVERAGE' : 1,
    #     }
    # ],
    # ['Field 1_0001_ch1_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2023_12_22_M1/',
    #     'DISTORTION_TYPE' : 'TRANSLATION',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 1,
    #     'NUMBER_OF_REF_FRAMES' : 20,
    #     'MOVING_AVERAGE' : 40,
    #     }
    # ],
    # ['Field 1_0001_ch2_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2023_12_22_M1/',
    #     'DISTORTION_TYPE' : 'TRANSLATION',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 1,
    #     'NUMBER_OF_REF_FRAMES' : 20,
    #     'MOVING_AVERAGE' : 40,
    #     }
    # ],

    # ['Field 1_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2023_12_22_M2/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 30,
    #     }
    # ],
    # ['Field 1_0001_ch2_registered_',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2023_12_22_M2/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 30,
    #     }
    # ],

    # ['Field_1',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_02_M3/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 30,
    #     }
    # ],
    # ['Field_2_0001_DRS_part',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_02_M3/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 30,
    #     }
    # ],
    # ['Field_2_0001_drug_part',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_02_M3/',
    #     'DISTORTION_TYPE' : 'TRANSLATION',
    #     'REFERENCE_FRAME' : 'previous',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 20,
    #     }
    # ],
    # ['Field_2_0001_drug_part_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_02_M3/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 30,
    #     }
    # ],

    # ['Field_1',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_05_M4/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 40,
    #     }
    # ],
    # ['Field_2_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_05_M4/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 20,
    #     }
    # ],

    # ['Field_2',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_08_M5/',
    #     'DISTORTION_TYPE' : 'AFFINE',
    #     'REFERENCE_FRAME' : 'previous',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 1,
    #     }
    # ],
    # ['Field_2_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_08_M5/',
    #     'DISTORTION_TYPE' : 'AFFINE',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 380,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],
    # ['Field_3_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_08_M5/',
    #     'DISTORTION_TYPE' : 'AFFINE',
    #     'REFERENCE_FRAME' : 'previous',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 1,
    #     }
    # ],
    # ['Field_3_0001_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_08_M5/',
    #     'DISTORTION_TYPE' : 'AFFINE',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 200,
    #     'MOVING_AVERAGE' : 120,
    #     }
    # ],

    # ['Field_1',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_10_M6/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],
    # ['Field_2',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_10_M6/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],
    # ['Field_3_ch1',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_10_M6/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 200,
    #     'MOVING_AVERAGE' : 20,
    #     }
    # ],
    # ['Field_3_ch2',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_10_M6/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],

    # ['Field_1',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_12_M7/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],
    # ['Field_2_ch1',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_12_M7/',
    #     'DISTORTION_TYPE' : 'AFFINE',
    #     'REFERENCE_FRAME' : 'previous',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 1,
    #     }
    # ],
    # ['Field_2_ch1_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_12_M7/',
    #     'DISTORTION_TYPE' : 'SCALED_ROTATION',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 220,
    #     'MOVING_AVERAGE' : 100,
    #     }
    # ],
    # ['Field_2_ch1',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_12_M7/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 1,
    #     'READ_TRANSFORM_MATRIX' : True,
    #     }
    # ],

    # ['Field_2_ch2',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_12_M7/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 200,
    #     'MOVING_AVERAGE' : 50,
    #     }
    # ],

    # ['Field_1',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_13_M8/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],
    # ['Field_2_ch1',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_13_M8/',
    #     'DISTORTION_TYPE' : 'SCALED_ROTATION',
    #     'REFERENCE_FRAME' : 'previous',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 1,
    #     'MOVING_AVERAGE' : 1,
    #     }
    # ],
    # ['Field_2_ch1_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_13_M8/',
    #     'DISTORTION_TYPE' : 'AFFINE',
    #     'REFERENCE_FRAME' : 'previous',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 100,
    #     'MOVING_AVERAGE' : 100,
    #     }
    # ],
    # ['Field_2_ch2',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_13_M8/',
    #     'DISTORTION_TYPE' : 'AFFINE',
    #     'REFERENCE_FRAME' : 'previous',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 1,
    #     'MOVING_AVERAGE' : 1,
    #     }
    # ],
    # ['Field_2_ch2_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_13_M8/',
    #     'DISTORTION_TYPE' : 'AFFINE',
    #     'REFERENCE_FRAME' : 'previous',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 100,
    #     'MOVING_AVERAGE' : 100,
    #     }
    # ],


    # ['Field_1_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/',
    #     'DISTORTION_TYPE' : 'TRANSLATION',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 100,
    #     'MOVING_AVERAGE' : 100,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],
    # ['Field_2_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/',
    #     'DISTORTION_TYPE' : 'TRANSLATION',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 100,
    #     'MOVING_AVERAGE' : 100,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],
    # ['Field_3',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/',
    #     'DISTORTION_TYPE' : 'TRANSLATION',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 100,
    #     'MOVING_AVERAGE' : 100,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],
    # ['Field_4',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/',
    #     'DISTORTION_TYPE' : 'TRANSLATION',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 100,
    #     'MOVING_AVERAGE' : 100,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],
    # ['Field_5',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/',
    #     'DISTORTION_TYPE' : 'TRANSLATION',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 100,
    #     'MOVING_AVERAGE' : 100,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],
    # ['Field_6',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/',
    #     'DISTORTION_TYPE' : 'AFFINE',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 100,
    #     'MOVING_AVERAGE' : 40,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],
    # ['Field_7_0001_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 100,
    #     'MOVING_AVERAGE' : 100,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],

    # ['Field_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_5_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field 7_trp_activators_application_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_23/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 100,
    #     'MOVING_AVERAGE' : 100,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],


    # ['Field_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_trp_activators_application_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M1/',
    #     'DISTORTION_TYPE' : 'TRANSLATION',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 20,
    #     'MOVING_AVERAGE' : 100,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],
    # ['Field_4_trp_activators_application_0001_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M1/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 1,
    #     'NUMBER_OF_REF_FRAMES' : 20,
    #     'MOVING_AVERAGE' : 40,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],


    # ['Field_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_trp_activators_application_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_24_M2/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 50,
    #     'MOVING_AVERAGE' : 150,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],

    # ['Field_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_trp_activators_application_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_25/',
    #     'DISTORTION_TYPE' : 'TRANSLATION',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 20,
    #     'MOVING_AVERAGE' : 70,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],
    # ['Field_2_trp_activators_application_0001_ch1_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_25/',
    #     'DISTORTION_TYPE' : 'AFFINE',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 70,
    #     'MOVING_AVERAGE' : 200,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],
    # ['Field_2_trp_activators_application_0001_ch2_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_25/',
    #     'DISTORTION_TYPE' : 'AFFINE',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 70,
    #     'MOVING_AVERAGE' : 200,
    #     'READ_TRANSFORM_MATRIX' : True,
    #     }
    # ],

    # ['Field_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_enlarged_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_7_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_8_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_trp_activators_application_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 1,
    #     'NUMBER_OF_REF_FRAMES' : 30,
    #     'MOVING_AVERAGE' : 50,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     # 'READ_TRANSFORM_MATRIX' : True,
    #     }
    # ],
    # ['Field_9_trp_activators_application_0001_ch1_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 3,
    #     'MOVING_AVERAGE' : 1,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],
    # ['Field_9_trp_activators_application_0001_ch2_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_29/',
    #     'READ_TRANSFORM_MATRIX' : True,
    #     }
    # ],

    # ['Field_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_05_01/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_05_01/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_0001',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_05_01/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 100,
    #      'MOVING_AVERAGE': 100,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],
    # ['Field_4_trp_activators_application_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_05_01/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 1,
    #     'NUMBER_OF_REF_FRAMES' : 20,
    #     'MOVING_AVERAGE' : 50,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],




    # ['Field_2_trp_activators_application_0001',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_22/',
    #      'DISTORTION_TYPE': 'TRANSLATION',
    #      'REFERENCE_FRAME': 'previous',
    #      'REFERENCE_CHANNEL': 1,
    #      'NUMBER_OF_REF_FRAMES': 20,
    #      'MOVING_AVERAGE': 150,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_2_trp_activators_application_0001_ch1_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_22/',
    #      'DISTORTION_TYPE': 'RIGID_BODY',
    #      'REFERENCE_FRAME': 'first',  # mb previous better
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 30,
    #      'MOVING_AVERAGE': 80,
    #      'READ_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_2_trp_activators_application_0001_ch1_registered_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_22/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 30,
    #      'MOVING_AVERAGE': 1,
    #      'READ_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_2_trp_activators_application_0001_ch1_registered_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_22/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 50,
    #      'MOVING_AVERAGE': 50,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],


    # ['Field_2_trp_activators_application_0001_ch1_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_22/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 20,
    #     'MOVING_AVERAGE' : 50,
    #     'SAVE_TRANSFORM_MATRIX' : True,
    #     }
    # ],

    # ['Field_2_trp_activators_application_0001_ch2_registered',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_22/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'REFERENCE_CHANNEL' : 0,
    #     'NUMBER_OF_REF_FRAMES' : 20,
    #     'MOVING_AVERAGE' : 50,
    #     'READ_TRANSFORM_MATRIX' : True,
    #     }
    # ],

    # ['Field_1_trp_activators_application_ch2',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_23_M1/',
    #     #  'DISTORTION_TYPE': 'TRANSLATION',
    #     #  'REFERENCE_FRAME': 'first',
    #     #  'REFERENCE_CHANNEL': 1,
    #     #  'NUMBER_OF_REF_FRAMES': 50,
    #     #  'MOVING_AVERAGE': 250,
    #      'READ_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_1_trp_activators_application_ch2',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_23_M1/',
    #      'DISTORTION_TYPE': 'TRANSLATION',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 1,
    #      'NUMBER_OF_REF_FRAMES': 50,
    #      'MOVING_AVERAGE': 250,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_1_trp_activators_application_ch1_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_23_M1/',
    #      'DISTORTION_TYPE': 'AFFINE',
    #      'REFERENCE_FRAME': 'previous',
    #      'REFERENCE_CHANNEL': 1,
    #      'NUMBER_OF_REF_FRAMES': 50,
    #      'MOVING_AVERAGE': 2,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_1_trp_activators_application_ch1_registered_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_23_M1/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 1,
    #      'NUMBER_OF_REF_FRAMES': 20,
    #      'MOVING_AVERAGE': 150,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],


    # ['Field_1_trp_activators_application_ch2',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_23_M1/',
    #      'DISTORTION_TYPE': 'TRANSLATION',
    #      'REFERENCE_FRAME': 'previous',
    #      'REFERENCE_CHANNEL': 1,
    #      'NUMBER_OF_REF_FRAMES': 20,
    #      'MOVING_AVERAGE': 150,
    #      'READ_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_1_trp_activators_application_0003_0001',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_23_M2/',
    #      'DISTORTION_TYPE': 'TRANSLATION',
    #      'REFERENCE_FRAME': 'previous',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 20,
    #      'MOVING_AVERAGE': 150,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_1_trp_activators_application_0003_0001_ch2_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_23_M2/',
    #      'DISTORTION_TYPE': 'RIGID_BODY',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 40,
    #      'MOVING_AVERAGE': 180,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_1_trp_activators_application_0003_0001_ch2_registered_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_23_M2/',
    #      'DISTORTION_TYPE': 'RIGID_BODY',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 40,
    #      'MOVING_AVERAGE': 10,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_1_trp_activators_application_0003_0001_ch1_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_07_23_M2/',
    #      'DISTORTION_TYPE': 'RIGID_BODY',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 40,
    #      'MOVING_AVERAGE': 10,
    #      'READ_TRANSFORM_MATRIX': True,
    #  }
    #  ],



    # ['Field_1_trp_activators_application_ch1',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/',
    #      'DISTORTION_TYPE': 'RIGID_BODY',
    #      'REFERENCE_FRAME': 'first',
    #      'NUMBER_OF_REF_FRAMES': 1,
    #      'MOVING_AVERAGE': 1,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],
    # ['Field_1_trp_activators_application_ch1_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/',
    #      'DISTORTION_TYPE': 'RIGID_BODY',
    #      'REFERENCE_FRAME': 'first',
    #      'NUMBER_OF_REF_FRAMES': 1,
    #      'MOVING_AVERAGE': 1,
    #      'READ_TRANSFORM_MATRIX': True,
    #  }
    #  ],
    # ['Field_1_trp_activators_application_ch1_registered_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/',
    #      'DISTORTION_TYPE': 'RIGID_BODY',
    #      'REFERENCE_FRAME': 'first',
    #      'NUMBER_OF_REF_FRAMES': 1,
    #      'MOVING_AVERAGE': 1,
    #      'READ_TRANSFORM_MATRIX': True,
    #  }
    #  ],


    # ['Field_1_trp_activators_application_ch2_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'NUMBER_OF_REF_FRAMES': 150,
    #      'MOVING_AVERAGE': 250,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],
    # ['Field_1_trp_activators_application_ch2_registered_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/',
    #      'DISTORTION_TYPE': 'TRANSLATE',
    #      'REFERENCE_FRAME': 'first',
    #      'NUMBER_OF_REF_FRAMES': 5,
    #      'MOVING_AVERAGE': 1,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],
    # ['Field_1_trp_activators_application_ch2_registered_registered_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'NUMBER_OF_REF_FRAMES': 13,
    #      'MOVING_AVERAGE': 1,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],


    # ['Field_1_trp_activators_application_ch1',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/',
    #      'DISTORTION_TYPE': 'RIGID_BODY',
    #      'REFERENCE_FRAME': 'first',
    #      'NUMBER_OF_REF_FRAMES': 1,
    #      'MOVING_AVERAGE': 1,
    #      'READ_TRANSFORM_MATRIX': True,
    #  }
    #  ],
    # ['Field_1_trp_activators_application_ch2_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_16/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'NUMBER_OF_REF_FRAMES': 10,
    #      'MOVING_AVERAGE': 200,
    #      'READ_TRANSFORM_MATRIX': True,
    #  }
    #  ],



    # ['Field_1_trp_activators_application_ch1',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M1/',
    #      'DISTORTION_TYPE': 'RIGID_BODY',
    #      'REFERENCE_FRAME': 'first',
    #      'MOVING_AVERAGE': 1,
    #      'READ_TRANSFORM_MATRIX': True,
    #  }
    #  ],
    # ['Field_1_trp_activators_application_ch1_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M1/',
    #      'DISTORTION_TYPE': 'AFFINE',
    #      'REFERENCE_FRAME': 'first',
    #      'NUMBER_OF_REF_FRAMES': 20,
    #      'MOVING_AVERAGE': 40,
    #      'READ_TRANSFORM_MATRIX': True,
    #  }
    #  ],


    # ['Field_1_trp_activators_application_ch2',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M1/',
    #      'DISTORTION_TYPE': 'RIGID_BODY',
    #      'REFERENCE_FRAME': 'first',
    #      'NUMBER_OF_REF_FRAMES': 1,
    #      'MOVING_AVERAGE': 1,
    #      'READ_TRANSFORM_MATRIX': True,
    #  }
    #  ],
    # ['Field_1_trp_activators_application_ch2_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M1/',
    #      'DISTORTION_TYPE': 'AFFINE',
    #      'REFERENCE_FRAME': 'first',
    #      'NUMBER_OF_REF_FRAMES': 20,
    #      'MOVING_AVERAGE': 40,
    #      'READ_TRANSFORM_MATRIX': True,
    #  }
    #  ],




    # ['Field_1_trp_activators_application',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M2/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 10,
    #      'MOVING_AVERAGE': 10,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],
    # ['Field_1_DRS',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_17_M2/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 10,
    #      'MOVING_AVERAGE': 10,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_11_trp_activators_application_0001',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 10,
    #      'MOVING_AVERAGE': 10,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_11_DRS_0001',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 10,
    #      'MOVING_AVERAGE': 10,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_8_trp_activators_application_0001',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 10,
    #      'MOVING_AVERAGE': 10,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],

    # ['Field_9_DRS_0001',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 10,
    #      'MOVING_AVERAGE': 10,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],



    # ['Field_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_07/',
    #         'DISTORTION_TYPE': 'TRANSLATION',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_07/',
    #         'DISTORTION_TYPE': 'TRANSLATION',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/',
    #         'DISTORTION_TYPE': 'AFFINE',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/',
    #         'DISTORTION_TYPE': 'AFFINE',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_7',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_8',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_11',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_12',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_13',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],


    # ['Field_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_7',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_8',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_11',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_12',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_13',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_14',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_15',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_08_M3/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_7',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_8',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_11',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_12',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_12_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_12_3',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_13',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_13_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_14',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_14_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'TRANSLATION',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_14_3',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_15',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_16',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_17',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_18',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_10/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],


    # ['Field_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_7',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_8',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_3',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_4',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_5',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_6',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_7',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_8',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_9',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_10',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10_3',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10_4',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10_5',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10_6',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10_7',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10_8',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10_9',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10_10',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_11',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_12',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_13',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_14',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_15',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_15_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_15_3',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_16',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_11/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_3',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_4',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_6',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_7',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2024_10_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],














    # ['Field_1_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_7_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_8_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_12_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_13_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_14_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],



    # ['Field_4_PI_0002',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_7_PI_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_11_18_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],




    # ['Field_2_DRS',
    #     {
    #         'DIRECTORY': 'D:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2025_02_07/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_DRS',
    #     {
    #         'DIRECTORY': 'D:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2025_02_07/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_DRS',
    #     {
    #         'DIRECTORY': 'D:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2025_02_07/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5_DRS',
    #     {
    #         'DIRECTORY': 'D:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2025_02_07/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6_DRS+CNQX+AP5_0001',
    #     {
    #         'DIRECTORY': 'D:/Lab Work Files/2-photon/Presynaptic inhibition Pirt GCamp3/2025_02_07/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
























    # ['TRP activators movie variant 2 2.434426229508197x.tif (red)',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/Projects/TRP project/Paper preparing/Supplements/TRP Activators/',
    #         'DISTORTION_TYPE': 'TRANSLATION',
    #         'REFERENCE_FRAME': 'first',
    #         'NUMBER_OF_REF_FRAMES': 4,
    #         'MOVING_AVERAGE': 1,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['TRP activators movie variant 2 2.434426229508197x.tif (green)',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/Projects/TRP project/Paper preparing/Supplements/TRP Activators/',
    #         'DISTORTION_TYPE': 'TRANSLATION',
    #         'REFERENCE_FRAME': 'first',
    #         'NUMBER_OF_REF_FRAMES': 4,
    #         'MOVING_AVERAGE': 1,
    #         'READ_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['TRP activators movie RGB_1.5x.tif (red)',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/Projects/TRP project/Paper preparing/Supplements/TRP Activators/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'NUMBER_OF_REF_FRAMES': 4,
    #         'MOVING_AVERAGE': 1,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['TRP activators movie RGB_1.5x.tif (green)',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/Projects/TRP project/Paper preparing/Supplements/TRP Activators/',
    #         'DISTORTION_TYPE': 'TRANSLATION',
    #         'READ_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # # MCU-KO project:
    # # Pirt_GCamp3 x MCU-KO + DRS + Caps:

    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_24_M1/4 A+C and C - 0.1 Hz',
    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_24_M1/5 A+C and C - 0.1 Hz',
    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_24_M1/6 A+C and C - 0.1 Hz_0001',
    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_24_M1/7',
    # ['8_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_24_M1/',
    #     'DISTORTION_TYPE' : 'AFFINE',
    #     'REFERENCE_FRAME' : 'previous',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ]



    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_24_M2/3_0001',

    # ['2',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M3/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 30,
    #     }
    # ]
    # ['3',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M3/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 30,
    #     }
    # ]
    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M3/4',
    # ['6_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M3/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 20,
    #     }
    # ]

    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M4/1_0000',
    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M4/1_0001',
    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M4/2_0001',

    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_30_M5/1_0000',
    # ['1_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_30_M5/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 20,
    #     }
    # ]
    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_30_M5/3_0001',

    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_01_M6/2',
    # ['3',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_01_M6/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 20,
    #     }
    # ]
    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_01_M6/5_0001',

    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_02_M7/1',

    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_03_M8/1_0000',
    # ['1_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_03_M8/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 30,
    #     }
    # ]
    # 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_03_M8/1_0002',



    # # C5a complement project:
    # # Pirt GCamp3 x Thy1 RGeco SNI or SHAM + DRS + PMX205 + Bicuculine:
    #

    # ['A_0015',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco SNI or SHAM + DRS  + PMX205 + Bicuculine/22_02_2023/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 20,
    #     }
    # ],
    # ['A_0016',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco SNI or SHAM + DRS  + PMX205 + Bicuculine/22_02_2023/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],
    # 'SNI_SHAM + PMX205/22_02_2023/A_0017',
    # 'SNI_SHAM + PMX205/22_02_2023/A_0018',
    # 'SNI_SHAM + PMX205/22_02_2023/A_0019',
    #
    # 'SNI_SHAM + PMX205/23_02_2023_M1/A_0008',
    # ['A_0008',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco SNI or SHAM + DRS  + PMX205 + Bicuculine/23_02_2023_M2/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 20,
    #     }
    # ],

    # 'SNI_SHAM + PMX205/23_02_2023_M1/A_0009',
    # 'SNI_SHAM + PMX205/23_02_2023_M1/A_0010',
    # 'SNI_SHAM + PMX205/23_02_2023_M1/A_0011',
    #
    # 'SNI_SHAM + PMX205/23_02_2023_M2/A_0007',
    # 'SNI_SHAM + PMX205/23_02_2023_M2/A_0008',
    # 'SNI_SHAM + PMX205/23_02_2023_M2/A_0009',
    # 'SNI_SHAM + PMX205/23_02_2023_M2/A_0010',
    #
    # 'SNI_SHAM + PMX205/24_02_2023/A_0015',
    # 'SNI_SHAM + PMX205/24_02_2023/A_0016',
    # 'SNI_SHAM + PMX205/24_02_2023/A_0017',
    # 'SNI_SHAM + PMX205/24_02_2023/A_0018',
    #
    # 'SNI_SHAM + PMX205/27_02_2023_M1/A_0005',
    # 'SNI_SHAM + PMX205/27_02_2023_M1/A_0006',
    # 'SNI_SHAM + PMX205/27_02_2023_M1/A_0008',
    # 'SNI_SHAM + PMX205/27_02_2023_M1/A_0009',
    #
    # 'SNI_SHAM + PMX205/27_02_2023_M2/A_0009',
    # 'SNI_SHAM + PMX205/27_02_2023_M2/A_0010',
    # 'SNI_SHAM + PMX205/27_02_2023_M2/A_0011',
    # 'SNI_SHAM + PMX205/27_02_2023_M2/A_0012',
    #
    # 'SNI_SHAM + PMX205/28_02_2023/A_0001',
    # 'SNI_SHAM + PMX205/28_02_2023/A_0002',
    # 'SNI_SHAM + PMX205/28_02_2023/A_0003',
    # 'SNI_SHAM + PMX205/28_02_2023/A_0004',










    # # Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine:
    #
    # ['A_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_01/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],
    # ['A',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_14/',
    #     'DISTORTION_TYPE' : 'AFFINE',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],
    # ['A_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_14/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 20,
    #     }
    # ],
    # ['A_0003',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_14/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 20,
    #     }
    # ],
    # ['A_0004',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_14/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 20,
    #     }
    # ],
    # ['A_0003',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_05/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],
    # ['A_0005',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_09/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],
    # ['08_03_2023_0002',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2023_03_08/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],
    # ['09_03_2023_0002',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2023_03_09/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 20,
    #     }
    # ],






    # # C5a complement project:
    # # Pirt GCamp3 x Thy1 RGeco + DRS + C5a:

    # ['A_0002_0001',
    #     {
    #     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + C5a/2022_12_28/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],







    # # TRPV1 Cre x GCamp5g TdT + Capsaicin:
    #
    # 'TRPV1 Cre x GCamp5g TdT + Capsaicin/06_04_2023_M1/06_04_2023_0003',
    # 'TRPV1 Cre x GCamp5g TdT + Capsaicin/06_04_2023_M2/__0001',









    # # Organoid project:
    #
    # ['Organoids/Alzheimer mRuby applications_0001', {'DIRECTORY' : 'F:/Lab Work Files/2-photon/'}],
    # 'Organoids/Control mRuby applications_0001',
    # ['Organoids/Alzheimer mtRGeco applications_0001', {'DIRECTORY' : 'F:/Lab Work Files/2-photon/'}],
    # 'Organoids/Control mtRGeco applications_0001',









    # # C5a complement project:
    # # Microglia + C5a:

    # 'Microglia + C5a/21_11_2022/B_0002',
    # 'Microglia + C5a/21_11_2022/C_0002',
    # 'Microglia + C5a/21_11_2022/D_0001',
    # 'Microglia + C5a/21_11_2022/E_0002',
    # 'Microglia + C5a/21_11_2022/E_0003',

    # 'Microglia + C5a/24_11_2022/Field 11',

    # 'Microglia + C5a/25_11_2022/Field 4_0001',
    # 'Microglia + C5a/25_11_2022/Field 7_0001',

    # 'Microglia + C5a/2023_11_17/1_0000',
    # 'Microglia + C5a/2023_11_17/4_0001',

    # 'Microglia + C5a/2023_11_20/B',
    # 'Microglia + C5a/2023_11_20/C_0001',
    # 'Microglia + C5a/2023_11_20/D_0001',
    # ['E_0001', {'DIRECTORY' : 'F:/Lab Work Files/2-photon/Microglia + C5a/2023_11_20/', 'DISTORTION_TYPE' : 'BILINEAR', 'REFERENCE_FRAME' : 'first', 'REFERENCE_CHANNEL' : 2, 'NUMBER_OF_REF_FRAMES' : 20, 'MOVING_AVERAGE' : 20,}],

    # 'Microglia + C5a/2023_11_21/A_overview_3_0001',
    # 'Microglia + C5a/2023_11_21/C_0002',
    # 'Microglia + C5a/2023_11_21/D',
    # 'Microglia + C5a/2023_11_21/F',
    # 'Microglia + C5a/2023_11_21/G_0001',








    # # HSD2-brainstem-slices


    # ['Slice_1_Angiotensin_application',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/HSD2-brainstem-slices/2025_06_23/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Slice_2_Angiotensin_application',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/HSD2-brainstem-slices/2025_06_23/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],


    # ['Slice_1_Angiotensin_application',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/HSD2-brainstem-slices/2025_07_23/',
    #         'DISTORTION_TYPE': 'TRANSLATION',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 1,
    #         'MOVING_AVERAGE': 1,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],




    # ['Slice_1b_Angiotensin_application',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/HSD2-brainstem-slices/2025_07_24_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 10,
    #         'MOVING_AVERAGE': 5,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Slice_2_Angiotensin_application',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/HSD2-brainstem-slices/2025_07_24_M1/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 3,
    #         'MOVING_AVERAGE': 3,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],


    # ['Slice_1_Angiotensin_DCZ_application_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/HSD2-brainstem-slices/2025_07_24_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 3,
    #         'MOVING_AVERAGE': 3,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Slice_2_Angiotensin_DCZ_application',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/HSD2-brainstem-slices/2025_07_24_M2/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 3,
    #         'MOVING_AVERAGE': 3,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],




    # ['Field_1_Caps_activators_application',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Thy1-RGeco control/2025_07_28/',
    #         'DISTORTION_TYPE': 'TRANSLATION',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 10,
    #         'MOVING_AVERAGE': 5,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_1_Caps_activators_application',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Thy1-RGeco control/2025_07_29_M1/',
    #         'DISTORTION_TYPE': 'TRANSLATION',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 1,
    #         'NUMBER_OF_REF_FRAMES': 10,
    #         'MOVING_AVERAGE': 5,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_1_Caps_activators_application',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/Thy1-RGeco control/2025_07_30/',
    #         'DISTORTION_TYPE': 'TRANSLATION',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 1,
    #         'NUMBER_OF_REF_FRAMES': 10,
    #         'MOVING_AVERAGE': 5,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_1_Caps_activators_application',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/Thy1-RGeco control/2025_08_04_M1/',
    #      'DISTORTION_TYPE': 'TRANSLATION',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 10,
    #      'MOVING_AVERAGE': 5,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],


    # ['Field_1_Caps_activators_application_0001',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/Thy1-RGeco control/2025_08_04_M2/',
    #      'DISTORTION_TYPE': 'TRANSLATION',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 1,
    #      'MOVING_AVERAGE': 1,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],
    # ['Field_1_Caps_activators_application_0001_ch1_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/Thy1-RGeco control/2025_08_04_M2/',
    #      'DISTORTION_TYPE': 'BILINEAR',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 0,
    #      'NUMBER_OF_REF_FRAMES': 3,
    #      'MOVING_AVERAGE': 1,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],


    # ['Field_1_Caps_activators_application_0001_ch1_registered',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/Thy1-RGeco control/2025_08_04_M2/',
    #      'DISTORTION_TYPE': 'AFFINE',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 1,
    #      'NUMBER_OF_REF_FRAMES': 10,
    #      'MOVING_AVERAGE': 15,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],
    # ['Field_1_Caps_activators_application',
    #  {
    #      'DIRECTORY': 'F:/Lab Work Files/2-photon/Thy1-RGeco control/2025_08_04_M3/',
    #      'DISTORTION_TYPE': 'TRANSLATION',
    #      'REFERENCE_FRAME': 'first',
    #      'REFERENCE_CHANNEL': 1,
    #      'NUMBER_OF_REF_FRAMES': 10,
    #      'MOVING_AVERAGE': 5,
    #      'SAVE_TRANSFORM_MATRIX': True,
    #  }
    #  ],
]


if __name__ == '__main__':
    import stackreg
    stackreg.main()
