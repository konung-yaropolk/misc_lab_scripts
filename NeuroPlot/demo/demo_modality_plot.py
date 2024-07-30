#!/usr/bin/env python

import NeuroPlot.parse_csv as csv
import NeuroPlot.modality_plot as plt

import os

if __name__ == '__main__':

    # input files in the demo folder:
    files = [
        'demo_data\modality_C_boutons.csv',
        # 'demo_data\modality_C_fibers.csv',
        # 'demo_data\modality_A_boutons.csv',
        # 'demo_data\modality_A_fibers.csv',
    ]

    for file in files:

        # Get full path of input files
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, file)

        # Parse data from csv file
        new_csv = csv.LoadCsv(file_path)
        data, binarization = new_csv.ParseCsv()

        # Make figure:
        plot = plt.ModalityPlot(data,
                                binarization,
                                modalities=[
                                    'ASP', 'CIM', 'Caps'],
                                angles=[90, 210, 330],
                                labels=False,
                                scalecircle=0.3,
                                marker='',
                                linestyle='-',
                                linewidth=0.7,
                                alpha=0.5,
                                same_scale=False,
                                colors=(
                                    'tab:green',
                                    'navy',
                                    'tab:red',
                                    'tab:cyan',
                                    'darkorange',
                                    'tab:purple',
                                    'black'))

        plot.show()
