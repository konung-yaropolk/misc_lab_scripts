import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('1_DRS_[-0s ; +0s].csv')
first_column = df.columns[0]
df[first_column] = df[first_column] - df[first_column].iloc[0]

# For each column in the dataframe, excluding the first one
for i, column in enumerate(df.columns[1:], start=1):
    # Create a new figure
    plt.figure()
    plt.figure(figsize=(15, 5), dpi=200)
    plt.style.use("ggplot")

    plt.text(0, 4.1,
'''Electrical stimulation:

DRS   A 10Hz 0.6s
DRS A+C 10Hz 0.6s
DRS   C 10Hz 0.6s''',
         size=7,
         bbox=dict(boxstyle='square',
                   ec='black',
                   fc='white',)
         )

    plt.suptitle('ASP 50uM      CIM 50uM      Caps 100nM')

    plt.axvline(32, color='gray', linestyle=":", linewidth=0.5)
    plt.axvline(61, color='gray', linestyle=":", linewidth=0.5)
    plt.axvline(97, color='gray', linestyle=":", linewidth=0.5)


    plt.fill_between(
        df[df.columns[0]],
        -0.2,
         0.2,
        where=(
            df[df.columns[0]] >= 0) & (df[df.columns[0]] <= 2800),
        color='black',
        alpha=0.1
    )


    plt.fill_between(
        df[df.columns[0]],
        -1,
        5,
        where=(
            df[df.columns[0]] >= 507) & (df[df.columns[0]] <= 983),
        color='green',
        alpha=0.1
    )

    plt.fill_between(
        df[df.columns[0]],
        -1,
        5,
        where=(
            df[df.columns[0]] >= 1268) & (df[df.columns[0]] <= 1721),
        color='green',
        alpha=0.1
    )

    plt.fill_between(
        df[df.columns[0]],
        -1,
        5,
        where=(
            df[df.columns[0]] >= 2318) & (df[df.columns[0]] <= 2800),
        color='red',
        alpha=0.1
    )


    # Plot the data
    plt.plot(df[df.columns[0]], df[column], color='black', linewidth=0.5)

    # Set the Y-axis range
    plt.ylim(-1, 5)

    # Save the figure as a PNG file
    plt.savefig(f'rois/roi_{i}.jpg')

    plt.close()


