from PIL import Image
import numpy as np
import settings as s
import tifffile
import os
import re
from scipy.ndimage import gaussian_filter
from skimage import io


# Defaults:
PATH_PREFIX = s.PATH_PREFIX
RESP_DURATION = s.RESP_DURATION    # in s
STEP_DURATION = s.STEP_DURATION    # in s
N_EPOCHS = s.N_EPOCHS


class Movie():

    def __init__(self,
                 file_path,
                 start,                # in ms
                 movie_duration,       # in s
                 response_duration=RESP_DURATION,  # in s: expected response duration
                 filename_suffix='',
                 ):

        self.movie_duration = movie_duration
        self.file_path = PATH_PREFIX + file_path
        self.start = start
        self.response_duration = response_duration
        self.filename_suffix = filename_suffix


class Derivatives(Movie):

    def __init__(self,
                 file_path,
                 start,                # in ms
                 movie_duration,       # in s
                 response_duration=RESP_DURATION,  # in s: expected response duration
                 filename_suffix='',
                 drs_pattern=[[None], [None]],
                 step_duration=STEP_DURATION,
                 n_epochs=N_EPOCHS,
                 **misc,
                 ):
        super().__init__(file_path,
                         start,
                         movie_duration,
                         response_duration,
                         filename_suffix,
                         )

        self.drs_pattern = drs_pattern
        self.step_duration = step_duration
        self.n_steps = len(self.drs_pattern[0])
        self.n_epochs = n_epochs
        self.result = None
        self.n_frames = None

        # Open the TIFF image stack
        self.img = io.imread(self.file_path)
        # img = Image.open(file_path)
        # img = tiff.imread(file_path)  # Image.open(file_path)
        self.n_frames = len(self.img)
        self.sampling_interval = self.movie_duration / self.n_frames

        print('\nFile: {} \nMovie duration: {} \nn frames: {} \nSampling interval, s: {} \nTrigger time, s: {}'.format(
            self.file_path, self.movie_duration, self.n_frames, self.sampling_interval, self.start))

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

    def process_secuence(self,):

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

    def __init(self,
               path):
        self.path = path

    def Parse(self, path):

        with open('{}.txt'.format(path), 'r') as file:

            trigger = '"[Event '
            strings = file.readlines()

            string = strings[12]
            if not string.startswith('"T Dimension"'):
                raise ValueError

            n_slides = int(re.findall(r'\	"([^[]*), ', string)[0])
            t_duration = float(re.findall(r'- ([^[]*)\ \[', string)[0])
            t_resolution = t_duration/n_slides

            events = [
                (float(strings[i+2][15:-6])/1000) for i, line in enumerate(strings) if trigger in line
            ]

        return t_duration, events
