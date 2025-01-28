#!/usr/bin/env python3

import os
import re
import numpy as np
import pystackreg
import tifffile
import settings as s


def file_finder(path, pattern, nonrecursive=False):
    files_list = []  # To store the paths of .txt files

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(path):
        for filename in files:
            if re.search(pattern, filename):
                files_list.extend(
                    [filename[:-4]])

        if nonrecursive:
            break

    return files_list


def transform(
    img,
    sr,
    transform_matrix,
):

    out = sr.transform_stack(img, tmats=transform_matrix)
    out = out.astype(np.int16)

    return out


def register(
    img,
    sr,
    REFERENCE_FRAME,
    NUMBER_OF_REF_FRAMES,
    MOVING_AVERAGE,
    TIME_AXIS,
    verbose=False,
):

    transform_matrix = sr.register_stack(
        img,
        reference=REFERENCE_FRAME,
        n_frames=NUMBER_OF_REF_FRAMES,
        moving_average=MOVING_AVERAGE,
        axis=TIME_AXIS,
        verbose=verbose,
    )

    return transform_matrix


def process(
    file,
    DIRECTORY=s.DIRECTORY,
    DISTORTION_TYPE=s.DISTORTION_TYPE,
    REFERENCE_FRAME=s.REFERENCE_FRAME,
    NUMBER_OF_REF_FRAMES=s.NUMBER_OF_REF_FRAMES,
    MOVING_AVERAGE=s.MOVING_AVERAGE,
    TIME_AXIS=s.TIME_AXIS,
    SPLIT_ONLY=s.SPLIT_ONLY,
    REFERENCE_CHANNEL=s.REFERENCE_CHANNEL,
    SAVE_TRANSFORM_MATRIX=s.SAVE_TRANSFORM_MATRIX,
    READ_TRANSFORM_MATRIX=s.READ_TRANSFORM_MATRIX,
    verbose=False,
):

    match DISTORTION_TYPE:
        case 'TRANSLATION': sr = pystackreg.StackReg(pystackreg.StackReg.TRANSLATION)
        case 'RIGID_BODY': sr = pystackreg.StackReg(pystackreg.StackReg.RIGID_BODY)
        case 'SCALED_ROTATION': sr = pystackreg.StackReg(pystackreg.StackReg.SCALED_ROTATION)
        case 'AFFINE': sr = pystackreg.StackReg(pystackreg.StackReg.AFFINE)
        case 'BILINEAR': sr = pystackreg.StackReg(pystackreg.StackReg.BILINEAR)
        case _: sr = pystackreg.StackReg(pystackreg.StackReg.TRANSLATION)

    metadata = {
        ' Current File': DIRECTORY + file + '_registered',
        ' Original File': DIRECTORY + file,
        ' Transformation Matrix Used': READ_TRANSFORM_MATRIX,
        ' Transformations Applied': not SPLIT_ONLY,
        ' Software Used': 'https://github.com/konung-yaropolk/stackreg',
        ' TIME_AXIS': TIME_AXIS,
        ' REFERENCE_CHANNEL': REFERENCE_CHANNEL,
        ' DISTORTION_TYPE': DISTORTION_TYPE,
        ' REFERENCE_FRAME': REFERENCE_FRAME,
        ' NUMBER_OF_REF_FRAMES': NUMBER_OF_REF_FRAMES,
        ' MOVING_AVERAGE': MOVING_AVERAGE,

    }

    # Bad construction, to review:
    try:
        img = tifffile.imread(DIRECTORY + file + '.tif')
    except:

        try:
            img = tifffile.imread(DIRECTORY + file + '.tiff')
        except Exception as e:
            print('\n!!! ', DIRECTORY + file, '- File not found')
            return e

    try:

        print('\n>>> ', file, '- started working with the file...')
        # algorytm for 4-dimentional tiff:
        if img.ndim == 4:

            # Here is a bug - sometimes array shape must be (1, len(img[0]), 3, 0)

            if READ_TRANSFORM_MATRIX:
                transform_matrix = np.load(
                    DIRECTORY + file + '_transform_matrix.npy')
            else:
                transform_matrix_list = np.empty((1, len(img[0]), 4, 0))
                # print(img.shape)
                transform_matrix = np.array([])

            if not SPLIT_ONLY:    # Bad construction with SPLIT_ONLY, to review

                for ch in range(len(img)):
                    if verbose:
                        print('\n     Analyzing file:',
                              file, ', channel', ch + 1, '...')

                    if not READ_TRANSFORM_MATRIX:
                        transform_matrix_list = np.append(
                            transform_matrix_list,
                            [register(
                                img[ch],
                                sr,
                                REFERENCE_FRAME,
                                NUMBER_OF_REF_FRAMES,
                                MOVING_AVERAGE,
                                TIME_AXIS,
                                verbose=verbose,
                            )
                            ],
                            axis=-1,
                        )

                if not READ_TRANSFORM_MATRIX:
                    print(transform_matrix_list.shape)
                    transform_matrix = np.mean(
                        transform_matrix_list,
                        axis=0,
                    ) if not REFERENCE_CHANNEL else transform_matrix_list[REFERENCE_CHANNEL-1]

                    if SAVE_TRANSFORM_MATRIX:
                        np.save(
                            DIRECTORY + file + '_transform_matrix',
                            transform_matrix,
                            allow_pickle=False,
                            fix_imports=True,
                        )

            for ch in range(len(img)):

                if not SPLIT_ONLY:    # Bad construction with SPLIT_ONLY, to review

                    if verbose:
                        print('\n     Transforming file',
                              file, ', channel', ch + 1, '...')

                    out = transform(
                        img[ch],
                        sr,
                        transform_matrix,
                    )

                else:
                    out = img[ch]

                tifffile.imwrite(
                    '{}{}_ch{}{}.tif'.format(
                        DIRECTORY,
                        file,
                        ch + 1,
                        '_registered' if not SPLIT_ONLY else ''
                    ),
                    out,
                    imagej=True,
                    compression='zlib',
                    metadata=metadata,
                )

        # algorytm for 3-dimentional tiff:
        elif img.ndim == 3 and not SPLIT_ONLY:    # Bad construction with SPLIT_ONLY, to review

            if READ_TRANSFORM_MATRIX:
                transform_matrix = np.load(
                    DIRECTORY + file + '_transform_matrix.npy')
                print('Transform matrix found for this file')
            else:
                transform_matrix = np.array([])
                transform_matrix = register(
                    img,
                    sr,
                    REFERENCE_FRAME,
                    NUMBER_OF_REF_FRAMES,
                    MOVING_AVERAGE,
                    TIME_AXIS,
                    verbose=False,
                )

            if SAVE_TRANSFORM_MATRIX:
                np.save(
                    DIRECTORY + file + '_transform_matrix',
                    transform_matrix,
                    allow_pickle=False,
                    fix_imports=True,
                )

            out = transform(
                img,
                sr,
                transform_matrix,
            )

            if verbose:
                print('\n     Writing to file...')

            tifffile.imwrite(
                '{}{}_registered.tif'.format(
                    DIRECTORY,
                    file,
                ),
                out,
                imagej=True,
                compression='zlib',
                metadata=metadata,
            )

        elif img.ndim == 3 and SPLIT_ONLY == True:
            raise Exception(
                'SPLIT_ONLY option is activated, there is nothing to do with single-channel image file')

        else:
            raise Exception('Wrong TIFF format, or check TIME_AXIS parameter')

    except Exception as e:
        print('!!!  An error occured when processing {}:\n{}'.format(file, e))
        return e

    else:
        print('\n<<< ', file, '- File done!')

    # immediatly clearing memory used by np arrays
    finally:
        img = None
        del img
        transform_matrix_list = None
        del transform_matrix_list
        transform_matrix = None
        del transform_matrix
        out = None
        del out


def main():

    if s.TAKE_ALL_FILES:
        TODO_LIST = file_finder(s.DIRECTORY, r'.*\.tif')
    else:
        TODO_LIST = s.TODO_LIST

    if s.MULTIPROCESSING:

        import multiprocessing as mp

        cores = mp.cpu_count()          # CPU cores count
        files = len(TODO_LIST)        # Files to do count
        processes_limit = s.PROCESSES_LIMIT if s.PROCESSES_LIMIT else 100

        processes = min(cores, files,
                        processes_limit)
        try:
            pool = mp.Pool(processes)
        except ValueError:
            print('No one file listed, there is nothing to do.')
            return 0

        print('\nParallel processing mode activated:')
        print('Please, ensure if you have enough RAM for multiprocessing.')
        print('If processing went wrong, please, use PROCESSES_LIMIT option in the settings.py')
        print('{0} cpu cores per queue of {1} files found, pool of {2} processes created.'.format(
            cores, files, processes))

        results = [pool.apply_async(process, args=(line[0],) if isinstance(line, list) else (
            line,), kwds=line[1] if isinstance(line, list) else {}) for line in TODO_LIST]
        output = [p.get() for p in results]

        print('\nErrors:', output)

    else:

        for line in TODO_LIST:

            if isinstance(line, list):
                process(line[0], **line[1], verbose=True)
            else:
                process(line, verbose=True)

    print('\nSeries done!\n')


if __name__ == '__main__':
    main()
