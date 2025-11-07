import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.offsetbox
from matplotlib.lines import Line2D
import os


EVENTS = [
    32,
    61,
    97,
    [507, 983],
    [1268, 1721],
    [2318, 2800],
]

TITLE = 'ASP 50uM      CIM 50uM      Caps 100nM'
LABEL = '''

Electrical stimulation:

DRS   A 10Hz 0.6s
DRS A+C 10Hz 0.6s
DRS   C 10Hz 0.6s

'''

# Y_RANGE = [-1, 3]


class AnchoredHScaleBar(matplotlib.offsetbox.AnchoredOffsetbox):

    """ size: length of bar in data units
        extent : height of bar ends in axes units """

    def __init__(self, size=1, extent=0.01, label="", loc=2, ax=None,
                 pad=0.4, borderpad=0.5, ppad=0, sep=2, prop=None,
                 frameon=True, linekw={}, **kwargs):
        if not ax:
            ax = plt.gca()
        trans = ax.get_yaxis_transform()
        size_bar = matplotlib.offsetbox.AuxTransformBox(trans)
        line = Line2D([0, 0], [size, 0], **linekw)
        hline1 = Line2D([-extent/2., extent/2.], [0, 0], **linekw)
        hline2 = Line2D([-extent/2., extent/2.], [size, size], **linekw)
        size_bar.add_artist(line)
        size_bar.add_artist(hline1)
        size_bar.add_artist(hline2)

        txt = matplotlib.offsetbox.TextArea(label, )
        self.vpac = matplotlib.offsetbox.VPacker(children=[size_bar, txt],
                                                 align="center", pad=ppad, sep=sep)
        matplotlib.offsetbox.AnchoredOffsetbox.__init__(self, loc, pad=pad,
                                                        borderpad=borderpad, child=self.vpac, prop=prop, frameon=frameon,
                                                        **kwargs)


def plot(x, cols, savename, csv_file_path, offset=True, label=False, figsize=(15, 5), timeline='min', alpha=0.7):

    if timeline == 'min':
        coef = 60
        time = x/coef
        xlabel = 'Time, min'
    else:
        coef = 1
        time = x
        xlabel = 'Time, s'
    # Create a combined figure with vertically shifted traces
    plt.figure(figsize=figsize, dpi=200)
    # plt.style.use("ggplot")

    if isinstance(offset, bool):
        # Calculate the maximum amplitude across all traces
        max_amplitude = max(df[column].max() - df[column].min()
                            for column in cols)
        offset = max_amplitude

    if label == True:
        plt.text(0, offset * len(cols),
                 LABEL,
                 size=7,
                 bbox=dict(boxstyle='square',
                           ec='black',
                           fc='white',)
                 )

    # +/- noise bar
    # noise_range = 0.2
    # plt.fill_between(
    #     time,
    #     -noise_range,
    #     noise_range,
    #     where=(time <= time.iloc[-1]),
    #     color='black',
    #     alpha=0.1
    # )

    for event in EVENTS:
        if isinstance(event, int):
            plt.axvline(event/coef, color='gray', linestyle=":", linewidth=0.5)
        elif isinstance(event, list):
            plt.fill_between(
                time,
                -1,
                offset * len(cols) + 1,
                where=(time >= event[0]/coef) & (
                    time <= event[-1]/coef),
                color='green',
                alpha=0.1
            )

    # Plot each trace with vertical offset
    for i, column in enumerate(cols):
        shift = i * offset
        plt.plot(time, df[column] +
                 shift, color='k', label=column, linewidth=0.5, alpha=alpha)

    if offset:
        # Set y-tick labels divided by vertical_shift, starting from 1, and rounded to integers
        ax = plt.gca()
        # y_ticks = ax.get_yticks()
        # ax.set_yticks(y_ticks)
        # ax.set_yticklabels([f'{int(round(y / vertical_shift + 1))}' for y in y_ticks])

        # Remove y-axis ticks
        ax.set_yticks([])

        ob = AnchoredHScaleBar(size=1, label="1 ΔF/F₀", loc=2, frameon=False,
                               pad=1, sep=4, linekw=dict(color="black"),)
        ax.add_artist(ob)

        w_percent = (time.iloc[-1]/100)

        # ax.errorbar(-10*w_percent, -0.5,
        #             yerr=0.5,
        #             fmt='none',
        #             capsize=4,
        #             ecolor='k',
        #             linewidth=2,
        #             zorder=3)

        # plt.text(-10*w_percent, -1., '1 ΔF/F₀',  horizontalalignment='center',
        #          verticalalignment='top')

        for i, y in enumerate(cols):
            plt.text(-7*w_percent, (i*offset), f'{i+1}', horizontalalignment='center',
                     verticalalignment='bottom')

    plt.suptitle(TITLE)
    plt.xlabel(xlabel)
    # plt.ylabel("Amplitude + Offset")
    plt.ylim(-1, offset * len(cols) + 1)

    plt.tight_layout()
    # Save the combined figure
    plt.savefig(os.path.join(
        DIR, f'{csv_file_path}/{savename}.png'), transparent=True)
    plt.close()


# Get the directory of the current script
DIR = os.path.dirname(os.path.abspath(__file__))

# List all CSV files in the directory
csv_files = [f for f in os.listdir(DIR) if f.lower().endswith('.csv')]

# Print or use the list of CSV files
print("CSV files in directory:", csv_files)


for file in csv_files:
    file_path = os.path.join(DIR, file)
    location = file_path[:-4]
    os.makedirs(file_path[:-4], exist_ok=True)

    # Read the CSV file
    df = pd.read_csv(file_path)
    first_column = df.columns[0]

    # Normalize X-axis so it starts from 0
    df[first_column] = df[first_column] - df[first_column].iloc[0]
    df.rename(columns={first_column: 'Time'}, inplace=True)

    # plotting
    plot(df['Time'], df.columns[1:], 'roi_combined_stacked',
         location, offset=True, figsize=(10, 10))
    plot(df['Time'], df.columns[1:], 'roi_combined_overlap',
         location, offset=False, alpha=0.1)

    for i, column in enumerate(df.columns[1:], start=1):
        plot(df['Time'], [column], f'roi_{i}', location, offset=False)
