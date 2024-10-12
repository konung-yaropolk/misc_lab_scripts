import os
from PIL import Image
import numpy as np
import tifffile


class TifColorMerger():

    def __init__(self,
                 dir,
                 red_name_ending,
                 green_name_ending,
                 blue_name_ending,
                 OUTPUT_NAME_ENDING):
        self.dir = dir
        self.red_name_ending = red_name_ending
        self.green_name_ending = green_name_ending
        self.blue_name_ending = blue_name_ending
        self.OUTPUT_NAME_ENDING = OUTPUT_NAME_ENDING

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
        tifffile.imwrite(output_path, multi_channel_array,
                         imagej=True, metadata={'axes': 'CYX',
                                                'mode': 'composite'})

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
                        root, base_name + self.OUTPUT_NAME_ENDING)

                    self.__create_two_channel_image(
                        red_path, green_path, blue_path, output_path)
                    print(f"Created two-channel image: {output_path}")


DIR = '\path\to\file'

RED_NAME_ENDING = '_red.tif'
GRN_NAME_ENDING = '_grn.tif'
BLE_NAME_ENDING = '_blue.tif'

OUTPUT_NAME_ENDING = '_hyperstack.tif'


# Example usage
merger = TifColorMerger(DIR,
                        RED_NAME_ENDING,
                        GRN_NAME_ENDING,
                        BLE_NAME_ENDING,
                        OUTPUT_NAME_ENDING)

merger.process_directory()
