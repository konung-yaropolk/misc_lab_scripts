from PIL import Image
import numpy as np
# import tifffile as tiff
from scipy.ndimage import gaussian_filter
from skimage import io


class Movie():

    def __init__(self,
                 file_path,
                 start,                # in ms
                 movie_duration,       # in s
                 response_duration=2,  # in s: expected response duration
                 ):

        self.movie_duration = movie_duration
        self.file_path = file_path
        self.start = start
        self.response_duration = response_duration


class Derivatives(Movie):

    def __init__(self,
                 file_path,
                 start,                # in ms
                 movie_duration,       # in s
                 response_duration=2,  # in s: expected response duration
                 drs_pattern=[],
                 step_duration=None,
                 n_epochs=None,
                 ):
        super().__init__(file_path,
                         start,
                         movie_duration,
                         response_duration,
                         )

        self.drs_pattern = drs_pattern
        self.step_duration = step_duration
        self.n_steps = len(self.drs_pattern[0])
        self.n_epochs = n_epochs
        self.result = None
        self.n_frames = None

        # Open the TIFF image stack
        self.img = io.imread(file_path)
        # img = Image.open(file_path)
        # img = tiff.imread(file_path)  # Image.open(file_path)
        self.n_frames = len(self.img)
        self.sampling_interval = self.movie_duration / self.n_frames

        print('\nMovie duration: {} \nn frames: {} \nSampling interval: {}'.format(
            self.movie_duration, self.n_frames, self.sampling_interval))

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

    def calculate_single_response(self):

        start_frame = int((self.start / 1000) // self.sampling_interval)
        stop_frame = int(((self.start / 1000) + self.response_duration)
                         // self.sampling_interval)

        self.result = self.process_tiff_stack(start_frame, stop_frame)

        # return self.result

    def calculate_sequence_responses(self, count, interval, delay):

        sequence_stack = [
            self.process_tiff_stack(
                int(((self.start / 1000) + (i*interval) + delay) //
                    self.sampling_interval),
                int(((self.start / 1000) + (i*interval) + delay + self.response_duration) //
                    self.sampling_interval)
            ) for i in range(count)
        ]

        self.result = np.average(sequence_stack, axis=0)

        # return self.result

    def calc_sequence(self, i, filename_ending):
        # der = self.Derivatives(item[0], **item[1])
        self.calculate_sequence_responses(
            self.n_epochs,
            self.step_duration * self.n_steps,
            self.step_duration * i)
        self.save(self.file_path + filename_ending)

    def process_secuence(self,):

        for i, [A, C] in enumerate(zip(self.drs_pattern[0], self.drs_pattern[1])):
            match [A, C]:
                case [1, 1]:
                    print('\nSequence A+C:')
                    self.calc_sequence(i, '_DERIVATIVES_A+C.tif')
                case [1, 0]:
                    print('\nSequence A:')
                    self.calc_sequence(i, '_DERIVATIVES_A.tif')
                case [0, 1]:
                    print('\nSequence C:')
                    self.calc_sequence(i, '_DERIVATIVES_C.tif')
                case [0, 0]: pass

    def save(self, output_path):

        output = Image.fromarray(self.result)
        output.save(output_path, save_all=True,
                    compression="tiff_deflate")

        # def calculate_sequence_response(self, ):

        # class Fluorescence(Movie):

        #     def __init__(self, ):

        #         super()__init__()
