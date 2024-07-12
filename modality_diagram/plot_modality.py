import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import csv


FILES = [
            'modality_C_boutons.csv',
            'modality_C_fibers.csv',
            'modality_A_boutons.csv',
            'modality_A_fibers.csv',
        ]


def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [tuple(float(cell) if cell else 0 for cell in row) for row in reader]
    return data


def plot_vectors(data):
    # Convert degrees to radians
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

    amplitudes_list = []

    for point in data:
        if not all(x == 0 for x in point):
            # Calculate the resultant vector
            resultant = np.sum([point[i] * np.exp(1j * angles[i]) for i in range(3)])
            amplitudes_list.append(np.abs(resultant))

            # Color measurement
            hue = 1/np.angle(resultant)
            sat = np.abs(resultant)/max(amplitudes_list)
            color_hsv = ((1, 0, 0))

            ax.plot([0, np.angle(resultant)], [0, np.abs(resultant)], marker='none',  ls='-', color=mcolors.hsv_to_rgb(color_hsv), alpha=0.4)

    plt.show()


def main():
    for file in FILES:
        data = read_csv_file(file)
        plot_vectors(data)


if __name__ == '__main__':
    main()