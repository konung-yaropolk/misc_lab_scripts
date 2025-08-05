import pandas as pd
import matplotlib.pyplot as plt
import os

FILE = 'sample.csv'
EVENTS = [
    32,
    61,
    97,
    [507, 983],
    [1268, 1721],
    [2318, 2800],

]

Y_RANGE = [-1, 3]
TITLE = 'ASP 50uM      CIM 50uM      Caps 100nM'
LABEL = '''

Electrical stimulation:

DRS   A 10Hz 0.6s
DRS A+C 10Hz 0.6s
DRS   C 10Hz 0.6s

'''


# Read the CSV file
df = pd.read_csv(FILE)
first_column = df.columns[0]
df[first_column] = df[first_column] - df[first_column].iloc[0]

# For each column in the dataframe, excluding the first one
for i, column in enumerate(df.columns[1:], start=1):
    # Create a new figure
    plt.figure()
    plt.figure(figsize=(15, 5), dpi=200)
    plt.style.use("ggplot")

    plt.text(0, 4.1,
             LABEL,
             size=7,
             bbox=dict(boxstyle='square',
                       ec='black',
                       fc='white',)
             )

    plt.suptitle(TITLE)

    # +/- noise bar
    plt.fill_between(
        df[df.columns[0]],
        -0.2,
        0.2,
        where=(df[df.columns[0]] <= df[df.columns[0]].iloc[1]),
        color='black',
        alpha=0.1
    )

    for event in EVENTS:

        if isinstance(event, int):
            plt.axvline(event, color='gray', linestyle=":", linewidth=0.5)

        if isinstance(event, list):
            plt.fill_between(
                df[df.columns[0]],
                Y_RANGE[0],
                Y_RANGE[1],
                where=(
                    df[df.columns[0]] >= event[0]) & (df[df.columns[0]] <= event[-1]),
                color='green',
                alpha=0.1
            )

    # Plot the data
    plt.plot(df[df.columns[0]], df[column], color='black', linewidth=0.5)

    # Set the Y-axis range
    plt.ylim(*Y_RANGE)

    # Save the figure as a PNG file
    os.makedirs('rois', exist_ok=True)
    plt.savefig(f'rois/roi_{i}.jpg')

    plt.close()
