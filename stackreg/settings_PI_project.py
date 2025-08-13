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

MULTIPROCESSING = True
# Use all available CPU cores.
# Faster, but need much more RAM so can be unstable.

PROCESSES_LIMIT = 3
# Maximum size of multiprocessing pull
# Set the maximum of processes if there isn't enough RAM
# Set 0 or None to use as many processes as possible


TODO_LIST = [                   # list here quoted TIFF file names without .tiff extensions, separated by comma:


    # # PI project:

    # ['Field_1_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_2_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_3_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_5',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_4_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],


    # ['Field_5_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_6_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_6_Bradikinin_application_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    # #  ],
    # ['Field_7_Dynorphin_application_ch1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    # #  ],
    # ['Field_7_Dynorphin_application_ch2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'READ_TRANSFORM_MATRIX': True,
    #     }
    #  ],


















    # ['Field_1_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_14/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_14/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_14/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],




















    # ['Field_1_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_3_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],




    # ['Field_2_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    # #  ],
    # ['Field_7_Dynorphin_application_ch1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    # #  ],
    # ['Field_7_Dynorphin_application_ch2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_15/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'READ_TRANSFORM_MATRIX': True,
    #     }
    #  ],



























    # ['Field_1_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_3_0001_ch1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    # #  ],
    # ['Field_1_3_0001_ch2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'READ_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
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
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
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
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_7_Dynorphin_application_ch1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_7_Dynorphin_application_ch2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_20/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'READ_TRANSFORM_MATRIX': True,
    #     }
    #  ],













































    # ['Field_1_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_1_0001_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_1_0002',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
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
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
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
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_7_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_8_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_8_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_8_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_8_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
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
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_9_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
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
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_10_3_Bradikinin_application_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_11_Dynorphin_application_ch1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    # #  ],
    # ['Field_11_Dynorphin_application_ch2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_21/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'READ_TRANSFORM_MATRIX': True,
    #     }
    #  ],













    # ['Field_1_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_1_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],

    # ['Field_2_1_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_2_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_2_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],


    # ['Field_3_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_3_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
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
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
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
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_3_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_4_4_0001',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],


    # ['Field_5_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_5_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],


    # ['Field_6_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_6_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],


    # ['Field_7_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
    # ['Field_7_2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_25/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'REFERENCE_CHANNEL': 0,
    #         'NUMBER_OF_REF_FRAMES': 100,
    #         'MOVING_AVERAGE': 100,
    #         'SAVE_TRANSFORM_MATRIX': True,
    #     }
    #  ],
























]


if __name__ == '__main__':
    import stackreg
    stackreg.main()
