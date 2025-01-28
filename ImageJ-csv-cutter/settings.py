#!/usr/bin/env python3
'''
ImageJ-csv-cutter
MIT License
Copyright (c) 2023 konung-yaropolk

Simple tool for Calcium-imaging data preprocessing, based on timing-metadata from Olympus Fluoview sowtware
Given script reformats your ImageJ ROI cvs-multimeasurements, based on the events timing from Olympus Fluoview metadata.

Algorythm explanation:

1. Lists all of the .txt files (excluding .txt files that names starts with !) in all subdirectories of listed in DIRECTORIES pathes.
2. Collects event-timing metadata from correct-format metadatas (having T-dimentional axis)
3. lists all the .csv files, wich names starts the same as the collected metadata .txt file names and wich have the same full patch
4. creates subdirectories with the same names as each listed 'generic' .csv files
5. puts inside modified .csv files for each of listed 'generic' .csv files


List below directories containing data (tiff + txt), then simple run the script.

'''

# input parameters:

TIME_BEFORE_TRIG = 10
# start trace from this timepoint (s. before trigger), 0 - full trace

TIME_AFTER_TRIG = 30
# finish trace at this timepoint   (s. after trigger), 0 - full trace

BASELINE_DURATON = 10
# set this many sec. before trigger as baseline (make sense if RELATIVE_VALUES activated),
# 0 - take TIME_BEFORE_TRIG value

# set the minimum area in pixels for ROI to be included (perspective feature)
MINIMAL_AREA = 0

# output parameters:
RELATIVE_VALUES = True   # dF/F0 output format
CSV_DELIMITER = ','      # delimiter to be used when saving .csv
MEAN_COL_ORDER = 2  # default 2
COLS_PER_ROI = 4  # default 4

DIRECTORIES = [

    # 'D:/Lab/2P-data/',


]


if __name__ == '__main__':
    import main
    main.main()
