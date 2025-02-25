import os
import re
import csv
import numpy as np
import matplotlib.pyplot as plt
import tifffile
import AutoStatLib
from PIL import Image
from scipy.ndimage import gaussian_filter
import settings as s

# Defaults:
WORKING_DIR = s.WORKING_DIR

RESP_DURATION = s.RESP_DURATION    # in s
STEP_DURATION = s.STEP_DURATION    # in s
N_EPOCHS = s.N_EPOCHS


RELATIVE_VALUES = s.RELATIVE_VALUES
MEAN_COL_ORDER = s.MEAN_COL_ORDER
COLS_PER_ROI = s.COLS_PER_ROI
TIME_BEFORE_TRIG = s.TIME_BEFORE_TRIG
BASELINE_DURATON = s.BASELINE_DURATON
TIME_AFTER_TRIG = s.TIME_AFTER_TRIG


class Helpers():

    def save_tiff(self, output_path, data, metadata={}):

        # output = Image.fromarray(data)
        # output.save(output_path, save_all=True,
        #             compression="tiff_deflate",
        #             tiffinfo=metadata)

        # does not work for some reasons:
        # if data.ndim == 3 else np.array([data]).astype(np.float32)
        img = data.astype(np.float32)
        tifffile.imwrite(output_path, img,
                         imagej=True, compression='deflate', metadata=metadata)

    def transpose(self, matrix):
        rows = len(matrix)
        cols = max(len(row) for row in matrix)

        transposed = [[None] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(len(matrix[i])):
                transposed[j][i] = matrix[i][j]

        return transposed

    def transpose_autoballance(self, data):
        # Determine the maximum length of any row
        max_len = max(len(row) for row in data)
        # Fill shorter rows with None to make all rows equal in length
        balanced_data = tuple(
            list(row) + [None] * (max_len - len(row)) for row in data)
        # Transpose the matrix
        data_t = tuple(tuple(balanced_data[j][i] for j in range(
            len(balanced_data))) for i in range(max_len))
        return data_t


class Plot(Helpers):

    # def __init__():
    #     pass

    def barplot(self, data_samples, p=1, stars='ns', sd=0, mean=0, median=0, testname='', n=0, dependent=False):

        n_bars = len(data_samples)
        fig, ax = plt.subplots(figsize=(0.5 + 0.9*n_bars, 4))
        linewidth = 2

        # generate endless repeating colormap
        num_colors = 9
        cmap = plt.get_cmap('Set1')
        cmap_fill = plt.get_cmap('Pastel1')
        colors = [cmap(i / num_colors)
                  for i in range(num_colors)]
        colors_fill = [cmap_fill(i / num_colors)
                       for i in range(num_colors)]
        colors.insert(0, 'k')
        colors_fill.insert(0, '#AAAAAA')

        # save the dots x positions to connect them with lines later
        spread_pool = []
        for i, data in enumerate(data_samples):
            x = i + 1  # Bar position
            # Bars:
            ax.bar(x,
                   mean[i],
                   yerr=sd[i],
                   width=.75,
                   capsize=8,
                   ecolor='r',
                   edgecolor=colors[i % len(colors)],
                   facecolor=colors_fill[i % len(colors_fill)],
                   fill=True,
                   linewidth=linewidth,
                   zorder=1)
            # Data points:
            # Adjust random horizontal spread range
            spread = np.random.uniform(-.10, .10, size=len(data))
            spread_pool.append(tuple(i+x for i in spread))
            ax.plot(x,
                    median[i],
                    marker='x',
                    markerfacecolor='#00000000',
                    markeredgecolor='r',
                    markersize=10,
                    markeredgewidth=1)
            ax.plot(x,
                    mean[i],
                    marker='_',
                    markerfacecolor='#00000000',
                    markeredgecolor='r',
                    markersize=16,
                    markeredgewidth=1)

        spread_pool_t = self.transpose_autoballance(spread_pool)
        for i, data in enumerate(self.transpose_autoballance(data_samples)):
            # Connect scatter points with lines
            ax.plot(spread_pool_t[i], data, color='k', alpha=0.5,
                    marker='o', linewidth=1, linestyle='-' if dependent else '', zorder=1)

        # Significance bar and stars
        y_range = max([max(data) for data in data_samples])
        x1, x2 = 1, n_bars
        y, h, col = 1.05 * y_range, .05 * y_range, 'k'
        ax.plot([x1, x1, x2, x2], [y, y + h, y + h, y], lw=linewidth, c=col)
        ax.text((x1 + x2) * .5,
                y + h,
                '{}\n{}'.format(p, stars),
                ha='center',
                va='bottom',
                color=col,
                fontweight='bold')

        # Add subtitle
        fig.text(0.95, 0.0, '{}\nn={}'.format(testname, str(n)[1:-1] if not dependent else str(n[0])),
                 ha='right', va='bottom', fontsize=8, fontweight='bold')

        # Remove borders
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.spines['left'].set_visible(True)
        ax.xaxis.set_visible(False)

        # Adjust width of axis
        for tick in ax.get_yticklabels():
            tick.set_fontweight('bold')
        ax.tick_params(width=linewidth)
        ax.yaxis.set_tick_params(labelsize=12)
        ax.spines['left'].set_linewidth(linewidth)
        ax.tick_params(axis='both', which='both',
                       length=linewidth*2, width=linewidth)

        plt.tight_layout()
        # plt.show()

        return plt


class TracesCalc():

    def __init__(self,
                 file_path,
                 time_before_trig=TIME_BEFORE_TRIG,
                 time_after_trig=TIME_AFTER_TRIG,
                 baseline_duraton=BASELINE_DURATON,
                 relative_values=RELATIVE_VALUES,
                 mean_col_order=MEAN_COL_ORDER,
                 cols_per_roi=COLS_PER_ROI,
                 trig_number=1,
                 ):

        self.file_path = file_path
        self.path = os.path.split(self.file_path)[0]
        self.file = os.path.split(self.file_path)[1]

        self.time_before_trig = time_before_trig
        self.time_after_trig = time_after_trig
        self.baseline_duraton = baseline_duraton
        self.relative_values = relative_values
        self.mean_col_order = mean_col_order
        self.cols_per_roi = cols_per_roi

        self.trig_number = trig_number

        Parser = MetadataParser()
        self.events, self.sampling_interval, self.movie_duration = Parser.Parse(
            self.path, self.file_nosuffix)

        self.event = self.events[trig_number]
        self.event_name = self.events[trig_number][0]
        self.start = self.events[trig_number][1]

    def file_finder(self, pattern, nonrecursive=False):
        files_list = []  # To store the paths of .txt files

        # Walk through the directory and its subdirectories
        for root, _, files in os.walk(self.path):
            for filename in files:
                if re.search(pattern, filename):
                    files_list.append(
                        [root if root[-1] == '/' else root + '/', filename[:-4]])

            if nonrecursive:
                break

        return files_list

    def file_lister(self, pattern, nonrecursive=False):
        files = []

        if os.path.isdir(self.path):
            files.extend(
                self.file_finder(
                    pattern,
                    nonrecursive
                )
            )
        else:
            print("!!!    Fail: invalid path        ", self.path)

        return files

    def csv_write(self, csv_output, csv_path, csv_file, filename_suffix, subdir=False):

        if subdir:
            os.makedirs(csv_path + csv_file +
                        filename_suffix + '/', exist_ok=True)
            path = '{0}{1}{2}/{2}.csv'.format(
                csv_path,
                csv_file,
                filename_suffix,
            )

        else:
            path = '{0}/{2}.csv'.format(
                csv_path,
                csv_file,
                filename_suffix,
            )

        with open(path, 'w') as f:

            writer = csv.writer(f, delimiter=',',
                                lineterminator='\r',)
            for row in csv_output:
                writer.writerow(row)

    def find_time_index(self, content, time):
        content = (float(i)-time for i in list(zip(*content))[0])
        diffs = [abs(i) for i in content]
        index = diffs.index(min(diffs))

        return index

    def data_normalize(self, content, start, zero):
        content_normalized = []

        for column in content:
            baseline = column[start:zero]
            baseline_sum = sum((float(cell) for cell in baseline))
            baseline_len = len(baseline)
            mean = baseline_sum/baseline_len if baseline_len and baseline else 0

            column_normalized = [(float(cell)-mean) /
                                 mean if mean else 0 for cell in column]                 # dF/F0
            # column_normalized = [float(cell)/mean if mean else 1 for cell in column]   # dF/F

            content_normalized.append(column_normalized)

        return content_normalized

    def csv_cutter(self, content):
        timeline_zero = (float(i)-self.start for i in list(zip(*content))[0])

        start = self.find_time_index(
            content, self.start - self.time_before_trig) if self.time_before_trig else None

        start_bl = self.find_time_index(
            content, self.start - self.baseline_duraton) if self.baseline_duraton else start

        zero = self.find_time_index(content, self.start)

        end = self.find_time_index(
            content, self.start + self.time_after_trig) if self.time_after_trig else None

        content = list(zip(*content))[1:]
        content[:0] = [timeline_zero]

        if self.relative_values:
            content[1:] = self.data_normalize(content[1:], start_bl, zero)

        csv_output = list(zip(*content))[start:end]

        return csv_output

    def csv_transform(self,
                      content_raw,
                      ):

        mean_col = self.mean_col_order  # order of "Mean" col in measurments
        n_cols = self.cols_per_roi      # n of measurments for each ROI

        first_col = (str(i*self.sampling_interval)
                     for i in range(len(content_raw)))
        content = list(zip(*content_raw))[mean_col::n_cols]
        content[:0] = [first_col]
        content = list(zip(*content))[1:]

        return content

    def csv_read(self, csv_path, csv_file):

        with open(csv_path + csv_file + '.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            content_raw = tuple(reader)

        return content_raw

    def calculate_ampl_auc(self, start_bl, end_bl, start, end):

        matrix = np.array(self.transpose(self.csv_matrix))

        # Extract time vector and data traces
        x = matrix[0]
        traces = matrix[1:]

        # Indices for baseline and signal periods
        bl_indices = np.where((x >= start_bl) & (x <= end_bl))[0]
        sig_indices = np.where((x >= start) & (x <= end))[0]
        whole_step_indices = np.where((x >= start_bl) & (x <= end))[0]

        # Lists to store peak amplitudes and AUCs for each trace
        ampl_list = []
        auc_list = []
        raw_line_list = [x[whole_step_indices]-start]

        for trace in traces:
            # Calculate baseline
            baseline = np.mean(trace[bl_indices])
            # Baseline correction
            corrected_trace = trace - baseline
            # Peak amplitude in signal period
            ampl = np.max(corrected_trace[sig_indices])
            ampl_list.append(ampl)
            # AUC in signal period
            auc = np.trapz(corrected_trace[sig_indices], x[sig_indices])
            auc_list.append(auc)

            raw_line_list.append(corrected_trace[whole_step_indices])

        # Calculate mean amplitude and AUC across all traces
        ampl_mean_of_rois = np.mean(ampl_list)
        auc_mean_of_rois = np.mean(auc_list)

        return ampl_mean_of_rois, ampl_list, raw_line_list

    def calc_traces_sequence(self, i, filename_ending):

        count = self.n_epochs + self.start_from_epoch-1
        interval = self.step_duration * self.n_steps
        delay = self.step_duration * i
        start = self.start_from_epoch-1

        ampl_mean_of_rois_by_epoch, ampl_list_each_by_roi, raw_line_list = [

            [
                self.calculate_ampl_auc(
                    (i*interval) + delay - self.step_duration/4,
                    (i*interval) + delay,
                    (i*interval) + delay,
                    (i*interval) + delay + self.step_duration/2
                )[j] for i in range(start, count)
            ] for j in range(3)

        ]

        ampl_list_each_by_epoch = self.transpose(ampl_list_each_by_roi)
        ampl_mean_of_epochs_by_rois = [np.mean(epoch)
                                       for epoch in ampl_list_each_by_epoch]

        # result_transposed = self.transpose(result)

        # self.save_tiff(self.file_path + self.output_suffix +
        #                filename_ending, self.result, metadata=metadata)
        return ampl_mean_of_rois_by_epoch, ampl_mean_of_epochs_by_rois, ampl_list_each_by_roi, ampl_list_each_by_epoch, raw_line_list

    def detailed_stats(self, csv_path, csv_file):

        ac_name_ending = '_RESPONSES_A+C.csv'
        a_name_ending = '_RESPONSES_A.csv'
        c_name_ending = '_RESPONSES_C.csv'

        for i, [A, C] in enumerate(zip(self.drs_pattern[0], self.drs_pattern[1])):
            match [A, C]:
                case [1, 1]:
                    ac_ampl_mean_of_rois_by_epoch, ac_ampl_mean_of_epochs_by_rois, ac_ampl_list_each_by_roi, ac_ampl_list_each_by_epoch, ac_raw_line_list = self.calc_traces_sequence(
                        i, ac_name_ending)
                case [1, 0]:
                    a_ampl_mean_of_rois_by_epoch,  a_ampl_mean_of_epochs_by_rois,  a_ampl_list_each_by_roi,  a_ampl_list_each_by_epoch,  a_raw_line_list = self.calc_traces_sequence(
                        i, a_name_ending)
                case [0, 1]:
                    c_ampl_mean_of_rois_by_epoch,  c_ampl_mean_of_epochs_by_rois,  c_ampl_list_each_by_roi,  c_ampl_list_each_by_epoch,  c_raw_line_list = self.calc_traces_sequence(
                        i, c_name_ending)
                case [0, 0]: pass
                case [None, None]: pass
                # responses_each_by_roi, responses_each_by_epoch = self.calc_traces_sequence(
                # i, '_RESPONSES.csv')

        ampl_c_to_ac_ratio_mean_of_epochs_by_rois = np.array(c_ampl_mean_of_epochs_by_rois) / \
            np.array(ac_ampl_mean_of_epochs_by_rois)

        ampl_c_to_ac_ratio_rois_by_epoch = np.array(c_ampl_list_each_by_epoch) / \
            np.array(ac_ampl_list_each_by_epoch)

        self.plot_c_to_ac_ratio_rois_by_epoch(
            ampl_c_to_ac_ratio_rois_by_epoch, '{0}{1}/_rois_by_epoch_retio_c_to_ac_ratio_auto_.png'.format(
                csv_path, csv_file))

        # csv file of AC and C amplitudes by rois epochs average
        self.csv_write(self.transpose([ac_ampl_mean_of_epochs_by_rois,
                       c_ampl_mean_of_epochs_by_rois, ampl_c_to_ac_ratio_mean_of_epochs_by_rois]),
                       csv_path+csv_file, csv_file, '_by_rois_mean_of_epochs_AC_C_ampl_auto_')

        # # csv file of C/A+C amplitudes ratio by rois epochs average
        # self.csv_write(self.transpose([ampl_c_to_ac_ratio_mean_of_epochs_by_rois]),
        #                csv_path+csv_file, csv_file, '_by_rois_mean_of_epochs_C_to_AC_ratio_auto_')

        # plot_ac_c_roi_stats for all rois
        self.plot_ac_c_roi_stats(ac_ampl_mean_of_epochs_by_rois,
                                 c_ampl_mean_of_epochs_by_rois,
                                 '{0}{1}/_by_rois_AC_C_ampl_auto_.png'.format(
                                     csv_path, csv_file),
                                 dependent=True)

        # plot_ac_c_roi_stats for each roi during timeline
        for i in range(len(ac_ampl_list_each_by_epoch)):
            self.plot_ac_c_roi_stats(ac_ampl_list_each_by_epoch[i],
                                     c_ampl_list_each_by_epoch[i],
                                     '{0}{1}/_roi{2}_AC_C_ampl_auto_.png'.format(
                                         csv_path, csv_file, i+1))

        # plot_stacked_traces
        self.plot_stacked_traces(self.transpose(self.csv_matrix),
                                 '{0}{1}/_full_traces_stacked_by_rois_auto_.svg'.format(
                                     csv_path, csv_file), shift=np.amax(c_ampl_list_each_by_roi))

        # plot_traces_by_rois
        # for i in range(len(ac_raw_line_list)):
        #     self.plot_traces_by_rois(ac_raw_line_list[i],
        #                              c_raw_line_list[i],
        #                              '{0}{1}/_epoch{2}_AC_C_traces_auto_.png'.format(csv_path, csv_file[:], i+self.start_from_epoch))

    def plot_c_to_ac_ratio_rois_by_epoch(self, array, path):

        # Create the plot
        plt.figure(figsize=(15, 10))  # Set the figure size to 10x15 inches
        x = list(range(1, len(array[0])+1))

        for roi in array:
            plt.plot(x, roi, marker='o', linestyle='-',
                     color='k')

        plt.title('C / A+C resp amplitude ratio')
        plt.xlabel('epoch')
        plt.ylabel('ROIs')
        plt.savefig(path)

    def plot_ac_c_roi_stats(self, group1, group2, path, dependent=False):

        data = [group1, group2]

        # set the parameters:
        paired = True   # is groups dependend or not
        tails = 2        # two-tailed or one-tailed result
        popmean = 0        # population mean - only for single-sample tests needed

        # initiate the analysis
        analysis = AutoStatLib.StatisticalAnalysis(
            data, paired=paired, tails=tails, popmean=0, verbose=False)

        analysis.RunMannWhitney()
        results = analysis.GetResult()

        plot = Plot()

        plt = plot.barplot(data,
                           p=results['p-value'],
                           stars=results['Stars_Printed'],
                           sd=results['Groups_SD'],
                           mean=results['Groups_Mean'],
                           median=results['Groups_Median'],
                           testname=results['Test_Name'],
                           n=results['Groups_N'],
                           dependent=dependent,
                           )

        plt.savefig(path)
        plt.close()

    def plot_traces_by_rois(self, array1, array2, path):
        plt.figure()

        # Plot lines from the first array in black
        x = array1[0]
        for y in array1[1:]:
            plt.plot(x, y, 'k-', alpha=.5)

        # Plot lines from the second array in red
        x = array2[0]
        for y in array2[1:]:
            plt.plot(x, y, 'r-', alpha=.5)

        plt.savefig(path)
        plt.close()

    def plot_stacked_traces(self, array, path, shift=1.2):
        plt.figure(figsize=(10, 10))

        x = array[0]

        for i, y in enumerate(array[1:]):
            shifted_y = [val + i * shift for val in y]
            plt.plot(x, shifted_y, 'k-', linewidth=0.7, alpha=1)

        # Set y-tick labels divided by shift, starting from 1, and rounded to integers
        ax = plt.gca()
        # y_ticks = ax.get_yticks()
        # ax.set_yticks(y_ticks)
        # ax.set_yticklabels([f'{int(round(y / shift + 1))}' for y in y_ticks])

        # Remove y-axis ticks
        ax.set_yticks([])

        # Save the plot as plot.png
        plt.tight_layout()
        plt.savefig(path, transparent=True)
        plt.close()

    def csv_process(self, detailed_stats=True):
        csv_list = []
        csv_list.extend(
            self.file_lister(
                r'^' + re.escape(self.file_nosuffix) + r'.*\.csv$',
                nonrecursive=True
            )
        )

        # adding all trace overview file starting from almost 0 time point
        # metadata.insert(0,['ALL_TRACE', 5])

        if csv_list:

            for csv_path, csv_file in csv_list:
                content_raw = self.csv_read(csv_path, csv_file)
                content = self.csv_transform(content_raw)

                # For multievent movies:
                # for i, event in enumerate(self.events):
                #     csv_output = self.csv_cutter(content, *event)
                #     try:
                #         self.csv_write(csv_output, csv_path, csv_file)
                #     except PermissionError:
                #         print('       File actually opened:')
                #         continue

                self.csv_matrix = self.csv_cutter(content)
                try:
                    self.csv_write(self.csv_matrix, csv_path,
                                   csv_file, self.output_suffix + '_full_traces_auto_', subdir=True)
                except PermissionError:
                    print('       File actually opened:')
                    continue

                if detailed_stats:
                    self.detailed_stats(
                        csv_path, csv_file + self.output_suffix + '_full_traces_auto_')

            result = '***    Done: {} csv files for      {}'.format(
                len(csv_list), self.file_path)

        else:
            result = '---    Skip: no csv files for     {}'.format(
                self.file_path)

        csv_list = None
        print(result)
        return result


class DerivativesCalc(Helpers):

    def compute_gaussian_derivatives(self, image_stack, start, end, sigma):

        # Compute derivatives along z-axis
        dz = gaussian_filter(
            image_stack[start:end], sigma=sigma, order=[1, 0, 0])

        return dz

    def process_tiff_stack(self, start, end):

        assert end - start >= 2, '!!! Error: {} - Too small interval to differentiate between frames {} and {}. '.format(
            self.file_path, start, end)
        assert start > 0, '!!! Error: Set the correct timing'
        assert end < self.n_frames, '!!! Error: Timing is out of movie duration'

        start -= 1
        end -= 1

        print('Frames ', start, ':', end)

        # Initialize a list to store the derivative images
        derivatives = self.compute_gaussian_derivatives(
            self.img, start, end, 1.0)

        # Average the derivatives to create a single image
        output_derivative = np.average(np.maximum(derivatives, 0), axis=0)

        return output_derivative

    # def calculate_single_response(self):

    #     start_frame = int((self.start / 1000) // self.sampling_interval)
    #     stop_frame = int(((self.start / 1000) + self.response_duration)
    #                      // self.sampling_interval)

    #     self.result = self.process_tiff_stack(start_frame, stop_frame)

    #     # return self.result

    def average_sequence_responses(self, count, interval, delay, start=0):

        sequence_stack = [
            self.process_tiff_stack(
                int((self.start + (i*interval) + delay) //
                    self.sampling_interval),
                int((self.start + (i*interval) + delay + self.response_duration) //
                    self.sampling_interval)
            ) for i in range(count)
        ]
        print(f'\nTaken {count-start} epochs: {start + 1} to {count}')
        self.result = np.average(sequence_stack[start:], axis=0)

        # return self.result

    def calc_sequence(self, i, filename_ending):
        self.average_sequence_responses(
            self.n_epochs + self.start_from_epoch-1,
            self.step_duration * self.n_steps,
            self.step_duration * i,
            start=self.start_from_epoch-1)

        metadata = {
            'axes': 'YX',
            'min': 0,
            'max': np.max(self.result),
        }

        self.save_tiff(self.file_path + self.output_suffix +
                       filename_ending, self.result, metadata=metadata)

    def derivatives_calculate(self,):

        # Open the TIFF image stack
        self.img = tifffile.imread(self.file_path)
        self.n_frames = len(self.img)

        ac_name_ending = '_auto_DERIVATIVES_A+C.tif'
        a_name_ending = '_auto_DERIVATIVES_A.tif'
        c_name_ending = '_auto_DERIVATIVES_C.tif'

        for i, [A, C] in enumerate(zip(self.drs_pattern[0], self.drs_pattern[1])):
            match [A, C]:
                case [1, 1]:
                    print('\nSequence A+C:')
                    self.calc_sequence(i, ac_name_ending)
                case [1, 0]:
                    print('\nSequence A:')
                    self.calc_sequence(i, a_name_ending)
                case [0, 1]:
                    print('\nSequence C:')
                    self.calc_sequence(i, c_name_ending)
                case [0, 0]: pass
                case [None, None]: self.calc_sequence(
                    i, '_auto_DERIVATIVES.tif')

        merger = TifColorMerger(self.path,
                                self.file + self.output_suffix + ac_name_ending,
                                self.file + self.output_suffix + c_name_ending,
                                self.file + self.output_suffix + ac_name_ending,
                                self.file + self.output_suffix + '_auto_DERIVATIVES_C-green_A+C-magenta.tif',
                                self.output_suffix)

        merger.process_directory()
        del merger


class Movie(DerivativesCalc, TracesCalc):

    def __init__(self,
                 file_path,
                 output_suffix='',
                 response_duration=RESP_DURATION,
                 drs_pattern=[[None], [None]],
                 step_duration=STEP_DURATION,
                 n_epochs=N_EPOCHS,
                 start_from_epoch=1,
                 trig_number=1,
                 time_before_trig=TIME_BEFORE_TRIG,
                 time_after_trig=TIME_AFTER_TRIG,
                 baseline_duraton=BASELINE_DURATON,
                 relative_values=RELATIVE_VALUES,
                 mean_col_order=MEAN_COL_ORDER,
                 cols_per_roi=COLS_PER_ROI,
                 **misc):

        self.file_path = WORKING_DIR + file_path
        self.path = os.path.split(self.file_path)[0]
        self.file = os.path.split(self.file_path)[1]
        self.filename_suffix, self.file_nosuffix = self.__calculate_suffix_and_nosuffix(
            self.file_path)
        self.output_suffix = output_suffix

        self.response_duration = response_duration
        self.drs_pattern = drs_pattern
        self.step_duration = step_duration
        self.n_steps = len(self.drs_pattern[0])
        self.n_epochs = n_epochs
        self.start_from_epoch = start_from_epoch if start_from_epoch != 0 else 1
        self.trig_number = trig_number-1

        self.time_before_trig = time_before_trig
        self.time_after_trig = time_after_trig
        self.baseline_duraton = baseline_duraton
        self.relative_values = relative_values
        self.mean_col_order = mean_col_order
        self.cols_per_roi = cols_per_roi

        self.result = None
        self.n_frames = None

        Parser = MetadataParser()
        self.events, self.sampling_interval, self.movie_duration, self.n_frames = Parser.Parse(
            self.path, self.file_nosuffix)

        self.event = self.events[self.trig_number]
        self.event_name = self.events[self.trig_number][0]
        self.start = self.events[self.trig_number][1]

        print('\nFile: {} \nMovie duration: {} \nn frames: {} \nSampling interval, s: {} \nTrigger time, s: {}'.format(
            self.file_path, self.movie_duration, self.n_frames, self.sampling_interval, self.start))

    def __calculate_suffix_and_nosuffix(self, file_full_path):
        # Get the directory from the given file's full path

        file_full_path = os.path.abspath(
            os.path.normpath(os.path.splitext(file_full_path)[0]))

        dir_path = os.path.dirname(file_full_path)
        # Get the given file's name
        given_file = os.path.basename(file_full_path)

        # List all .txt files in the directory
        txt_files = [os.path.abspath(os.path.normpath(os.path.join(
            dir_path, f))) for f in os.listdir(dir_path) if f.endswith('.txt')]

        # Find the longest common prefix among the given file and txt files
        common_prefixes = [os.path.commonprefix(
            [file_full_path, txt_file]) for txt_file in txt_files]

        file_nosuffix_with_path = max(common_prefixes, key=len).rstrip('_')

        # Remove the directory path from the common prefix
        file_nosuffix = os.path.basename(file_nosuffix_with_path)

        # Determine the suffix from the given file
        filename_suffix = os.path.basename(
            file_full_path[len(file_nosuffix_with_path):])

        return filename_suffix, file_nosuffix


class TifColorMerger(Helpers):

    def __init__(self, dir, red_name_ending, green_name_ending, blue_name_ending, output_name_ending, output_suffix):
        self.dir = dir
        self.red_name_ending = red_name_ending
        self.green_name_ending = green_name_ending
        self.blue_name_ending = blue_name_ending
        self.output_name_ending = output_name_ending
        self.output_suffix = output_suffix

    def __create_two_channel_image(self, red_channel_path, green_channel_path, blue_channel_path, output_path):
        channels = []

        if red_channel_path:
            red_channel = Image.open(red_channel_path)
            red_array = np.array(red_channel).astype(np.float32)
            channels.append(red_array)

        if green_channel_path:
            green_channel = Image.open(green_channel_path)
            green_array = np.array(green_channel).astype(np.float32)
            channels.append(green_array)

        if blue_channel_path:
            blue_channel = Image.open(blue_channel_path)
            blue_array = np.array(blue_channel)
            channels.append(blue_array)

        # Stack the arrays along the first axis to create a multi-channel image
        multi_channel_array = np.stack(channels, axis=0)

        # Save the multi-channel image in ImageJ format
        try:
            self.save_tiff(output_path, multi_channel_array, metadata={
                           'axes': 'CYX', 'mode': 'composite'})
        except PermissionError as e:
            print('PermissionError:', e)

        # Save the image as a PNG file
        for i in range(3 - len(channels)):
            channels.append(np.zeros_like(channels[0]))

        channels = np.array(channels)
        rgb_array_normalized = np.stack(
            [(channel - channels.min()) / (channels.max() - channels.min()) for channel in channels], axis=-1)
        rgb_image = Image.fromarray(
            (rgb_array_normalized * 255).astype('uint8'), 'RGB')
        try:
            rgb_image.save(output_path[:-4] + '.png')
        except PermissionError as e:
            print('PermissionError:', e)

        # Crerating Heatmap
        # Calculate the ratio image if red and green channels are available
        if len(channels) >= 2:
            ratio_image = np.divide(channels[1], channels[0], out=np.zeros_like(
                channels[0]), where=channels[0] != 0)
            ratio_image = np.clip(ratio_image, 0, np.max(ratio_image))

            # Save the ratio image as a single-frame TIFF file with inferno LUT metadata
            output_heatmap_path = output_path[:-4] + \
                self.output_suffix + '_heatmap.tif'

            metadata = {
                'axes': 'YX',
                'min': 1,
                'max': 4,  # np.max(ratio_image) * 0.73
            }

            try:
                # tifffile.imwrite(output_heatmap_path, ratio_image.astype(np.float32), imagej=True, metadata=metadata)
                self.save_tiff(output_heatmap_path,
                               ratio_image, metadata=metadata)
                print(f"Created heatmap image: {output_heatmap_path}")

            except PermissionError as e:
                print('PermissionError:', e)

            # Save the ratio image as a heatmap in PNG format using matplotlib
            ratio_image = np.clip(ratio_image, 1, 4)
            output_heatmap_path = output_path[:-4] + \
                self.output_suffix + '_heatmap.png'
            enlarged_shape = (
                int(ratio_image.shape[1] * 1.0), int(ratio_image.shape[0] * 1.0))
            fig, ax = plt.subplots(
                figsize=(enlarged_shape[0] / 100, enlarged_shape[1] / 100), dpi=165)

            ax.imshow(ratio_image, cmap='inferno',
                      interpolation='bicubic', extent=[0, 1, 0, 1])
            ax.set_position([0.02, 0.02, 0.98, 0.98])
            ax.axis('off')
            fig.patch.set_facecolor('white')
            cbar = plt.colorbar(ax.imshow(
                ratio_image, cmap='inferno', interpolation='bicubic', extent=[0, 1, 0, 1]), ax=ax)
            cbar.set_label('C to A+C responses ratio',
                           rotation=90, labelpad=5)
            plt.savefig(output_heatmap_path, bbox_inches='tight', pad_inches=0)
            plt.close()

    def process_directory(self):
        for root, _, files in os.walk(self.dir):
            red_files = [f for f in files if f.endswith(self.red_name_ending)]
            green_files = [f for f in files if f.endswith(
                self.green_name_ending)]

            for red_file in red_files:
                base_name = red_file[:-len(self.red_name_ending)]
                matching_green_file = base_name + self.green_name_ending
                matching_blue_file = base_name + self.blue_name_ending

                if matching_green_file in green_files:
                    red_path = os.path.join(
                        root, red_file) if self.red_name_ending else None
                    green_path = os.path.join(
                        root, matching_green_file) if self.green_name_ending else None
                    blue_path = os.path.join(
                        root, matching_blue_file) if self.blue_name_ending else None
                    output_path = os.path.join(
                        root, base_name + self.output_name_ending)

                    self.__create_two_channel_image(
                        red_path, green_path, blue_path, output_path)
                    print("\nCreated hyperstack image: {}".format(output_path))


class MetadataParser():

    def Parse(self, path, file):

        with open('{}/{}.txt'.format(path, file), 'r') as file:

            trigger = '"[Event '
            strings = file.readlines()

            string = strings[12]
            if not string.startswith('"T Dimension"'):
                raise ValueError

            n_slides = int(re.findall(r'\	"([^[]*), ', string)[0])
            t_duration = float(re.findall(r'- ([^[]*)\ \[', string)[0])
            t_resolution = t_duration/n_slides

            events = [
                (strings[i+1][18:-2], float(strings[i+2][15:-6])/1000) for i, line in enumerate(strings) if trigger in line
            ]

        return events, t_resolution, t_duration, n_slides


def main():

    for item in s.TO_DO_LIST:

        print(' ')
        movie = Movie(item[0], **item[1])

        if s.RUN_DERIVATIVES_CALCULATION:
            # try:
            movie.derivatives_calculate()
            # except Exception as e:
            #     print(e)
            #     pass

        if s.RUN_TRACES_CALCULATION:
            movie.csv_process()
            pass

        del movie


if __name__ == '__main__':
    main()
