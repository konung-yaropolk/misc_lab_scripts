import numpy as np
from PIL import Image, ImageSequence
import os

script_dir = os.path.dirname(os.path.abspath(__file__))


def upscale_tiff_stack(script_dir, scale_factor):

    print('Started working in the script\'s dirrectory:')
    print(script_dir)

    for filename in os.listdir(script_dir):

        if filename.endswith(".tiff") or filename.endswith(".tif"):
            img_path = os.path.join(script_dir, filename)
            img = Image.open(img_path)

            frames = []
            for frame in ImageSequence.Iterator(img):
                frame = frame.convert("RGB")  # Ensure frame is in RGB mode

                # Upscale using Lanczos algorithm
                new_size = (int(frame.width * scale_factor),
                            int(frame.height * scale_factor))
                upscaled_frame = frame.resize(new_size, Image.LANCZOS)
                frames.append(upscaled_frame)

            # Save the upscaled image
            output_path = os.path.join(
                script_dir, '{}x_{}'.format(scale_factor, filename))
            frames[0].save(output_path, save_all=True,
                           append_images=frames[1:], compression="tiff_deflate")
            print(filename, 'done!')


scale_factor = 1.5  # Change this to your desired scale factor
upscale_tiff_stack(script_dir, scale_factor)
