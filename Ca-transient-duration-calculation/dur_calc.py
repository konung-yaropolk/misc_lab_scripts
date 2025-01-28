import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import e

sd_treshold = 5
trip_treshold = 1/e  # % of amplitude
plot = True


def interpolate_time(time, y_values, threshold, index1, index2):
    # Check if the indices are within the bounds
    if index1 < 0 or index2 >= len(time):
        return time[index1] if index1 >= 0 else time[index2]

    # Fetch the values for interpolation
    y1 = y_values[index1] if index1 >= 0 else None
    y2 = y_values[index2] if index2 < len(y_values) else None
    t1 = time[index1] if index1 >= 0 else None
    t2 = time[index2] if index2 < len(time) else None

    # Perform interpolation only if both values are present
    if y1 is not None and y2 is not None and t1 is not None and t2 is not None:
        t_cross = t1 + (threshold - y1) * (t2 - t1) / (y2 - y1)
        return t_cross
    else:
        # If any value is missing, return the existing point
        print('##############################     Peak longer then sample!\n\n')
        return t1 if y1 is not None else t2
    

def plot_curves(time, y_columns, durations, threshold_lines, output_file):
    plt.figure(figsize=(10, 6))
    
    for idx, col in enumerate(y_columns.columns):
        y_offset = y_columns[col] + idx * 1 # Apply vertical offset
        plt.plot(time, y_offset, label=f'Y{idx+1}')
        plt.axhline(y=idx * 1 + threshold_lines[col], color='#0008', linestyle=':')  # Threshold line
        duration_label = f'{durations[f"Y{idx+1}_duration"]:.2f}s' 
        plt.text(time.iloc[0], y_offset.iloc[-1], duration_label, verticalalignment='bottom')

    plt.xlabel('Time, s')
    plt.ylabel('dF/F0')
    plt.legend()
    plt.savefig(output_file)
    plt.close()


def calculate_duration(time, y_values):
    baseline = np.mean(y_values[y_values < 0])
    baseline_std = np.std(y_values[y_values < 0])
    peak_amplitude = np.max(y_values) - baseline
    print('\n', baseline, '-baseline')
    
    # Check if the peak amplitude is less than six standard deviations of baseline noise
    if peak_amplitude < sd_treshold * baseline_std:
        return 0  # Set duration to zero
    
    threshold = baseline + trip_treshold * peak_amplitude
    print(peak_amplitude, '-peak_amplitude')
    print(threshold, '-threshold')

    # Find where the signal crosses the threshold
    above_threshold = y_values >= threshold

    start_index = np.argmax(above_threshold)
    end_index = len(above_threshold) - np.argmax(above_threshold[::-1]) - 1

    # Interpolate to find exact crossing points
    t_start = interpolate_time(time, y_values, threshold, start_index - 1, start_index)
    t_end = interpolate_time(time, y_values, threshold, end_index, end_index + 1)

    duration = t_end - t_start    
    print(duration, '-duration')

    return round(duration, 4)

def main(input_file, output_suffix='_DURATIONS'):
    # Read the input CSV file
    df = pd.read_csv(input_file, header=None)

    # Extract time and Y columns
    time = df.iloc[:, 0]
    y_columns = df.iloc[:, 1:]

    # Calculate the duration of peaks for each Y column
    durations = {}
    threshold_lines = {}
    for idx, col in enumerate(y_columns.columns):
        baseline = np.mean(y_columns[col][y_columns[col] < 0])
        peak_amplitude = np.max(y_columns[col]) - baseline
        threshold_lines[col] = baseline + trip_treshold * peak_amplitude
        durations[f'Y{idx+1}_duration'] = calculate_duration(time, y_columns[col])

    # Create the output DataFrame
    output_df = pd.DataFrame(durations, index=[0])

    # Define the output file name
    output_file = input_file.rsplit('.', 1)[0] + output_suffix + '.csv'

    # Save the output DataFrame to a new CSV file
    output_df.to_csv(output_file, index=False)

    print(f'Processed data saved to {output_file}')

    # Plot curves and threshold lines if requested
    if plot:
        plot_file = input_file.rsplit('.', 1)[0] + output_suffix + '.png'
        plot_curves(time, y_columns, durations, threshold_lines, plot_file)
        print(f'Plot saved to {plot_file}')



queue = [

'2024_04_24_M2_A',
'2024_04_24_M2_C',
'2024_04_24_M2_N',

]

for file in queue:
    main(file)
