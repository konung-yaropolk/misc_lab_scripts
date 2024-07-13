import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np
import csv
import os


class CsvFile:
    '''
        The input CSV file must be comma delimited and aligned on three columns.
        Each column represents one modality. Empty cells are counted as 0.
        Each row containing at least one value will be represented as a point.
    '''

    def __init__(self, file: str) -> None:
        self.file = file

    def parse_csv_file(self) -> list:

        # Get dir where script is located
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, self.file)

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = [tuple(float(cell) if cell else 0 for cell in row)
                    for row in reader]

        return data


class ModalityPlotter:
    '''
        Input fotmat:

        data: list of points, each point should be represented as a 
              list or touple containing three floats, one per modality.

    '''

    def __init__(self,
                 data: list,
                 modalities=('1', '2', '3'),
                 angles=[90, 210, 330],
                 marker='',
                 ls='-',
                 linewidth=0.5,
                 alpha=0.8,
                 colors=(
                     'tab:green',
                     'tab:cyan',
                     'tab:olive',
                     'black',
                     'tab:blue',
                     'tab:purple',
                     'tab:red',),
                 normalization_func='sigmoid',
                 ) -> None:

        self.data = data
        self.modalities = modalities
        self.angles = np.deg2rad(angles)
        self.marker = marker
        self.ls = ls
        self.linewidth = linewidth
        self.alpha = alpha
        self.colors = colors
        self.normalization_func = normalization_func

    def normalization(self, input) -> list:
        ''' 
            Define function to normalize coordinates
            to values in range of 0 to 1 for HSV color model.
            input: np.array
        '''

        match self.normalization_func:

            case 'linear':
                def func(x): return (x - np.min(input)) / \
                    (np.max(input) - np.min(input))

            case 'sigmoid':
                def func(x): return 1 / (1 + np.exp(-x))

            # case 'log':
            #     log_input = np.log1p(input)
            #     func = lambda x: (x - np.min(log_input)) / (np.max(log_input) - np.min(log_input))

        return [func(x) for x in input]

    def resultants(self, data) -> list:

        resultants = []
        for point in data:
            # ignore empty lines
            if not all(x == 0 for x in point):
                # Calculate resultant vector
                resultants.append(
                    np.sum([point[i] * np.exp(1j * self.angles[i]) for i in range(len(point))]))
            else:
                resultants.append((0))

        return resultants

    def draw_subplot(self, ax, plot_pattern, modalities, color) -> None:

        resultants = self.resultants(self.data)

        # Color measurement in HSV format
        # hue_array = self.normalization(np.angle(resultants))
        # sat_array = np.ones_like(hue_array)
        # val_array = self.normalization(np.abs(resultants))

        # for resultant, hue, sat, val in zip(resultants, hue_array, sat_array, val_array):
        for resultant, row in zip(resultants, data):
            binarized_row = [bool(i) for i in row]

            if resultant and (binarized_row == plot_pattern):
                ax.plot(
                    [0, np.angle(resultant)],
                    [0, np.abs(resultant)],
                    marker='',
                    ls='-',
                    linewidth=self.linewidth,
                    color=color,  # mcolors.hsv_to_rgb((hue, sat, val)),
                    alpha=self.alpha)
                ax.set_xticklabels(modalities)

        # Plot the single-unit circle
        r = 1
        theta = np.linspace(0, 2*np.pi, 100)
        ax.plot(theta, [r]*len(theta), color='black', linewidth=1)

    def initiate_subplot(self, ax) -> None:

        # Set custom design
        ax.set_yticklabels([])
        ax.set_xticks(self.angles)
        ax.grid(False)
        ax.spines['polar'].set_visible(False)
        ax.patch.set_facecolor('none')

    # Draw coordinate grid on the top of figure
    # to make easier subplots alignment on devtime
    def debug_grid(self, fig, y, x) -> None:

        for i in range(1, y*x+1):
            ax = fig.add_subplot(y, x, i)

            # Set the facecolor of the axes
            ax.patch.set_facecolor('none')
            ax.set_xticks([])
            ax.set_yticks([])

            for spine in ax.spines.values():
                spine.set_edgecolor('black')

    # Main drawing method

    def draw(self) -> None:

        # Create figure
        fig = plt.figure(figsize=(10, 10))

        # Defining layout
        gs = gridspec.GridSpec(64, 56, figure=fig)
        ax1 = fig.add_subplot(gs[0:20, 18:38], polar=True)
        ax12 = fig.add_subplot(gs[16:28, 2:18], polar=True)
        ax13 = fig.add_subplot(gs[16:28, 38:54], polar=True)
        ax123 = fig.add_subplot(gs[17:49, 12:44], polar=True)
        ax2 = fig.add_subplot(gs[34:54, 0:20], polar=True)
        ax23 = fig.add_subplot(gs[50:62, 22:34], polar=True)
        ax3 = fig.add_subplot(gs[34:54, 36:56], polar=True)

        subplots = (
            # formatting accurate list, lol
            ax1,
            ax12,  ax13,
            ax123,
            ax2,   ax23,    ax3,
        )

        # columns = (
        #     [[row[0]] for row in self.data],
        #     [[row[0], row[1]] for row in self.data],
        #     [[row[0], row[2]] for row in self.data],
        #     self.data,
        #     [[row[1]] for row in self.data],
        #     [[row[1], row[2]] for row in self.data],
        #     [[row[2]] for row in self.data],
        # )

        plot_patterns = (
            [True, False, False],
            [True, True, False],
            [True, False, True],
            [True, True, True],
            [False, True, False],
            [False, True, True],
            [False, False, True],
        )

        modalities = (
            (self.modalities[0], None, None),
            (self.modalities[0], self.modalities[1], None),
            (self.modalities[0], None, self.modalities[2]),
            (None, None, None),  # self.modalities[:],
            (None, self.modalities[1], None),
            (None, self.modalities[1], self.modalities[2]),
            (None, None, self.modalities[2]),
        )

        for ax, plot_pattern, modalities, color in zip(subplots, plot_patterns, modalities, self.colors):
            self.initiate_subplot(ax)

            self.draw_subplot(ax, plot_pattern, modalities, color)

        # Draw coordinate grid on the top of figure
        # to make easier subplots alignment on devtime
        # self.debug_grid(fig, 28, 28)

        plt.subplots_adjust(wspace=0.0, hspace=0.0)
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':

    files = [   # drop files in the same folder:
                'modality_C_boutons.csv',
                # 'modality_C_fibers.csv',
                # 'modality_A_boutons.csv',
                # 'modality_A_fibers.csv',
    ]

    for file in files:
        new_csv = CsvFile(file)
        data = new_csv.parse_csv_file()

        plot = ModalityPlotter(data, modalities=['ASP', 'CIM', 'Caps'],)
        plot.draw()
