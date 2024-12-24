from PIL import Image
import numpy as np
import settings as s
import tifffile
import os
import re
import csv
from scipy.ndimage import gaussian_filter


# Defaults:
WORKING_DIR = s.WORKING_DIR
INPUT_NAME_SUFFIX = s.INPUT_NAME_SUFFIX
RESP_DURATION = s.RESP_DURATION    # in s
STEP_DURATION = s.STEP_DURATION    # in s
N_EPOCHS = s.N_EPOCHS


RELATIVE_VALUES = s.RELATIVE_VALUES
MEAN_COL_ORDER = s.MEAN_COL_ORDER
COLS_PER_ROI = s.COLS_PER_ROI
TIME_BEFORE_TRIG = s.TIME_BEFORE_TRIG
BASELINE_DURATON = s.BASELINE_DURATON
TIME_AFTER_TRIG = s.TIME_AFTER_TRIG


class TracesCalc():

    def __init__(self,
                 file_path,
                 time_before_trig=TIME_BEFORE_TRIG,
                 time_after_trig=TIME_AFTER_TRIG,
                 baseline_duraton=BASELINE_DURATON,
                 relative_values=RELATIVE_VALUES,
                 mean_col_order=MEAN_COL_ORDER,
                 cols_per_roi=COLS_PER_ROI,

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

    def csv_write(self, csv_output, csv_path, csv_file):

        os.makedirs(csv_path + csv_file + '_traces/', exist_ok=True)
        with open(
                '{0}{1}_traces/{1}_timeline.csv'.format(
                    csv_path,
                    csv_file,
                ),
                'w') as f:

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

    def csv_process(self):
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

                csv_output = self.csv_cutter(content)
                try:
                    self.csv_write(csv_output, csv_path, csv_file)
                except PermissionError:
                    print('       File actually opened:')
                    continue

            result = '***    Done: {} csv files for      {}'.format(
                len(csv_list), self.file_path)

        else:
            result = '---    Skip: no csv files for     {}'.format(
                self.file_path)

        csv_list = None
        print(result)
        return result


class DerivativesCalc():

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

    def average_sequence_responses(self, count, interval, delay):

        sequence_stack = [
            self.process_tiff_stack(
                int((self.start + (i*interval) + delay) //
                    self.sampling_interval),
                int((self.start + (i*interval) + delay + self.response_duration) //
                    self.sampling_interval)
            ) for i in range(count)
        ]

        self.result = np.average(sequence_stack, axis=0)

        # return self.result

    def calc_sequence(self, i, filename_ending):
        # der = self.Derivatives(item[0], **item[1])
        self.average_sequence_responses(
            self.n_epochs,
            self.step_duration * self.n_steps,
            self.step_duration * i)
        self.save(self.file_path + filename_ending)

    def derivatives_calculate(self,):

        for i, [A, C] in enumerate(zip(self.drs_pattern[0], self.drs_pattern[1])):
            match [A, C]:
                case [1, 1]:
                    print('\nSequence A+C:')
                    self.calc_sequence(
                        i, '_DERIVATIVES_A+C' + self.filename_suffix + '.tif')
                case [1, 0]:
                    print('\nSequence A:')
                    self.calc_sequence(i, '_DERIVATIVES_A' +
                                       self.filename_suffix + '.tif')
                case [0, 1]:
                    print('\nSequence C:')
                    self.calc_sequence(i, '_DERIVATIVES_C' +
                                       self.filename_suffix + '.tif')
                case [0, 0]: pass
                case [None, None]: self.calc_sequence(
                    i, '_DERIVATIVES_' + self.filename_suffix + '.tif')

    def save(self, output_path):

        output = Image.fromarray(self.result)
        output.save(output_path, save_all=True,
                    compression="tiff_deflate",
                    tiffinfo={})

        # def calculate_sequence_response(self, ):

        # class Fluorescence(Movie):

        #     def __init__(self, ):

        #         super()__init__()


class Movie(DerivativesCalc, TracesCalc):

    def __init__(self,
                 file_path,
                 response_duration=RESP_DURATION,
                 filename_suffix=INPUT_NAME_SUFFIX,
                 drs_pattern=[[None], [None]],
                 step_duration=STEP_DURATION,
                 n_epochs=N_EPOCHS,
                 trig_number=0,
                 time_before_trig=TIME_BEFORE_TRIG,
                 time_after_trig=TIME_AFTER_TRIG,
                 baseline_duraton=BASELINE_DURATON,
                 relative_values=RELATIVE_VALUES,
                 mean_col_order=MEAN_COL_ORDER,
                 cols_per_roi=COLS_PER_ROI,
                 **misc,
                 ):

        self.file_path = WORKING_DIR + file_path
        self.path = os.path.split(self.file_path)[0]
        self.file = os.path.split(self.file_path)[1]
        self.filename_suffix = filename_suffix
        self.file_nosuffix = self.file[:-len(self.filename_suffix)]
        self.response_duration = response_duration
        self.drs_pattern = drs_pattern
        self.step_duration = step_duration
        self.n_steps = len(self.drs_pattern[0])
        self.n_epochs = n_epochs
        self.trig_number = trig_number

        self.time_before_trig = time_before_trig
        self.time_after_trig = time_after_trig
        self.baseline_duraton = baseline_duraton
        self.relative_values = relative_values
        self.mean_col_order = mean_col_order
        self.cols_per_roi = cols_per_roi

        self.result = None
        self.n_frames = None

        Parser = MetadataParser()
        self.events, self.sampling_interval, self.movie_duration = Parser.Parse(
            self.path, self.file_nosuffix)

        self.event = self.events[trig_number]
        self.event_name = self.events[trig_number][0]
        self.start = self.events[trig_number][1]

        # Open the TIFF image stack
        self.img = tifffile.imread(self.file_path)
        self.n_frames = len(self.img)

        # self.sampling_interval = self.movie_duration / self.n_frames

        print('\nFile: {} \nMovie duration: {} \nn frames: {} \nSampling interval, s: {} \nTrigger time, s: {}'.format(
            self.file_path, self.movie_duration, self.n_frames, self.sampling_interval, self.start))


class TifColorMerger():

    def __init__(self,
                 dir,
                 red_name_ending,
                 green_name_ending,
                 blue_name_ending,
                 output_name_ending):
        self.dir = dir
        self.red_name_ending = red_name_ending
        self.green_name_ending = green_name_ending
        self.blue_name_ending = blue_name_ending
        self.output_name_ending = output_name_ending

    def __create_two_channel_image(self, red_channel_path, green_channel_path, blue_channel_path, output_path):
        channels = []

        if red_channel_path:
            red_channel = Image.open(red_channel_path)
            red_array = np.array(red_channel)
            channels.append(red_array)

        if green_channel_path:
            green_channel = Image.open(green_channel_path)
            green_array = np.array(green_channel)
            channels.append(green_array)

        if blue_channel_path:
            blue_channel = Image.open(blue_channel_path)
            blue_array = np.array(blue_channel)
            channels.append(blue_array)

        # Stack the arrays along the third axis to create a two-channel image
        multi_channel_array = np.stack(channels, axis=0)

        # Save the two-channel image in ImageJ format
        try:
            tifffile.imwrite(output_path, multi_channel_array,
                             imagej=True, metadata={'axes': 'CYX',
                                                    'mode': 'composite', })
        except PermissionError as e:
            print('PermissionError:', e)

        # Save the image as a PNG file
        for i in range(3-len(channels)):
            channels.append(np.zeros_like(channels[0]))

        channels = np.array(channels)
        rgb_array_normalized = np.stack([(channel-channels.min()) / (channels.max()-channels.min())
                                         for channel in channels], axis=-1)
        rgb_image = Image.fromarray(
            (rgb_array_normalized*255).astype('uint8'), 'RGB')
        try:
            rgb_image.save(output_path[:-3] + 'png')
        except PermissionError as e:
            print('PermissionError:', e)

    def process_directory(self):
        for root, _, files in os.walk(self.dir):
            red_files = [f for f in files if f.endswith(self.red_name_ending)]
            green_files = [f for f in files if f.endswith(
                self.green_name_ending)]

            for red_file in red_files:
                # Remove ending
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
                    print(f"Created hyperstack image: {output_path}")


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

        return events, t_resolution, t_duration


def main():

    for item in s.TO_DO_LIST:

        # try:
        print(' ')
        movie = Movie(item[0], **item[1])
        movie.derivatives_calculate()

        # except Exception as e:
        #     print(e)
        #     pass

    if s.RUN_TRACES_CALCULATION:
        movie.csv_process()
        pass

    if s.RUN_HYPERSTACK_COMPOSITOR:
        print(
            '\n\nHyperstack Compositor started in the directory: {}\n'.format(s.WORKING_DIR))

        merger = TifColorMerger(s.WORKING_DIR,
                                s.RED_NAME_ENDING,
                                s.GRN_NAME_ENDING,
                                s.BLE_NAME_ENDING,
                                s.OUTPUT_NAME_ENDING)

        merger.process_directory()


if __name__ == '__main__':
    main()
