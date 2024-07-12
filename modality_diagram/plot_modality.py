import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import csv
import os


class CsvFile:

    def __init__(self, file: str):
        self.file = file

    def parse_csv_file(self) -> list:

        # Get dir where script is located
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, self.file)

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = [tuple(float(cell) if cell else 0 for cell in row) for row in reader]

        return data


class ModalityPlotter:


    def __init__(self, data):
        self.data = data
        

    def normalization(self, input, func='sigmoid'):
        ''' Define function to normalize coordinates
            to values in range of 0 to 1 for HSV model
            input: np.array'''

        match func:

            case 'linear':
                func = lambda x: (x - np.min(input)) / (np.max(input) - np.min(input))        

            case 'sigmoid':
                func = lambda x: 1 / (1 + np.exp(-x))

            # case 'log':
            #     log_input = np.log1p(input)
            #     func = lambda x: (x - np.min(log_input)) / (np.max(log_input) - np.min(log_input))


        return [func(x) for x in input]


    def plot_vectors(self, data: list) -> None:

        # Convert deg to rads
        angles = np.deg2rad([90, 210, 330])

        # Create figure
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)

        # Set custom design
        ax.set_yticklabels([])
        ax.set_xticks(angles)
        ax.set_xticklabels(['ASP', 'CIM', 'Caps'])
        ax.grid(False)
        ax.spines['polar'].set_visible(False)

        resultants = []

        for point in data:

            # pass through empty lines
            if not all(x == 0 for x in point):

                # Calculate resultant vector
                resultants.append(np.sum([point[i] * np.exp(1j * angles[i]) for i in range(3)]))


        # Color measurement in HSV format
        hue_array = self.normalization(np.angle(resultants))
        sat_array = np.ones_like(hue_array)
        val_array = self.normalization(np.abs(resultants))

        for resultant, hue, sat, val in zip(resultants, hue_array, sat_array, val_array):
            ax.plot(
                [0, np.angle(resultant)],
                [0, np.abs(resultant)],
                marker='',
                ls='-',
                color=mcolors.hsv_to_rgb((hue, sat, val)),
                alpha=1
            )

        plt.show()


    def plot(self):
        self.plot_vectors(self.data)



if __name__ == '__main__':

    files = [   # drop files in the same folder:
                'modality_C_boutons.csv',
                'modality_C_fibers.csv',
                'modality_A_boutons.csv',
                'modality_A_fibers.csv',
            ]


    for file in files:      
        new_csv = CsvFile(file)
        data = new_csv.parse_csv_file()

        plotter = ModalityPlotter(data)
        plotter.plot()