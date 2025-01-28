from PIL import Image
import numpy as np
import os


def concatenate_tif_stacks(stack1_path, stack2_path, output_path):

    # designating the current directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Open the image stacks
    stack1 = Image.open(os.path.join(script_dir, stack1_path))
    stack2 = Image.open(os.path.join(script_dir, stack2_path))

    frames = []

    try:
        while True:
            # Convert frames to numpy arrays
            frame1 = np.array(stack1)
            frame2 = np.array(stack2)

            # Concatenate along the y-axis
            concatenated_frame = np.concatenate((frame1, frame2), axis=axis)

            # Convert back to PIL image and append to frames list
            frames.append(Image.fromarray(concatenated_frame))

            # Move to the next frame
            stack1.seek(stack1.tell() + 1)
            stack2.seek(stack2.tell() + 1)
    except EOFError:
        # End of file reached
        pass

    # Save the concatenated frames as a new TIFF stack
    frames[0].save(os.path.join(script_dir, output_path),
                   save_all=True, append_images=frames[1:])

# Concatenation axis (0 - verticaly)
# make sure that inputs are the same length along the axis of concatenation
axis=0
concatenate_tif_stacks('input1.tif',
                       'input2.tif',
                       'output.tif')
