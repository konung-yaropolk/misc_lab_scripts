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
                 start,
                 response_duration=2,
                 ):
        super().__init__(file_path,
                         start,
                         response_duration,
                         )
        self.result = None
        self.n_frames = None

        # Open the TIFF image stack
        self.img = io.imread(file_path)
        # img = Image.open(file_path)
        # img = tiff.imread(file_path)  # Image.open(file_path)
        self.n_frames = len(self.img)
        self.sampling_interval = self.movie_duration / self.n_frames

        print('Movie duration: {} \nn frames: {} \nSampling interval: {}'.format(
            self.movie_duration, self.n_frames, self.sampling_interval))

    def compute_gaussian_derivatives(self, image_stack, start, end, sigma):

        # Compute derivatives along z-axis
        dz = gaussian_filter(
            image_stack[start:end], sigma=sigma, order=[1, 0, 0])

        return dz

    def process_tiff_stack(self, start, end):

        assert end - start >= 2, '!!! Error: {} - Too small interval to differentiate between frames {} and {}. '.format(
            file_path, start, end)
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

        return self.result

    def save(self, output_path):

        output = Image.fromarray(self.result)
        output.save(output_path, save_all=True,
                    compression="tiff_deflate")

        # def calculate_sequence_response(self, ):

        # class Fluorescence(Movie):

        #     def __init__(self, ):

        #         super()__init__()


file_path = 'Field_6_registered.tif'

der = Derivatives(file_path, 22003, 246.167)
der.calculate_single_response()
der.save(file_path + '_DERIVATIVES.tif')
