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

PROCESSES_LIMIT = 10
# Maximum size of multiprocessing pull
# Set the maximum of processes if there isn't enough RAM
# Set 0 or None to use as many processes as possible


TODO_LIST = [                   # list here quoted TIFF file names without .tiff extensions, separated by comma:


    # specified parameters for eacj movie:

    # ['movie_0001',
    #     {
    #     'DIRECTORY' : 'D:/Lab/',
    #     'DISTORTION_TYPE' : 'BILINEAR',
    #     'REFERENCE_FRAME' : 'first',
    #     'NUMBER_OF_REF_FRAMES' : 10,
    #     'MOVING_AVERAGE' : 10,
    #     }
    # ],



    # apply default parameters for theese movies:

    # 'D:/Lab/movie_0001',
    # 'D:/Lab/movie_0002',
    # 'D:/Lab/movie_0003',


    # get movies from default folder if indicated in settings:

    # 'movie_0001',
    # 'movie_0002',
    # 'movie_0003',


]


if __name__ == '__main__':
    import stackreg
    stackreg.main()
