import plotter.modality_plot as plt
import plotter.parse_csv as csv


if __name__ == '__main__':

    files = [   # drop files in the same folder:
        'modality_C_boutons.csv',
        # 'modality_C_fibers.csv',
        # 'modality_A_boutons.csv',
        # 'modality_A_fibers.csv',
    ]

    for file in files:
        new_csv = csv.CsvFile(file)
        data, binarization = new_csv.parse_csv_file()
        plot = plt.ModalityPlot(data,
                                binarization,
                                modalities=['ASP', 'CIM', 'Caps'],
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
