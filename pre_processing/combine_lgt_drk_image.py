'''
combine the light and dark image side by side for easy visualization
'''


import os
import cv2
import numpy as np

def get_image_side_by_side(image_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
    results = []  # Store results for the batch

    for filename in os.listdir(image_dir):
        if filename.endswith('light.png'):
            # Paths for light and dark images
            light_image_file = os.path.join(image_dir, filename)
            dark_image_file = os.path.join(image_dir, filename.replace('light', 'dark'))
            output_image_path = os.path.join(output_dir, filename.replace('light.png', 'lightdark.png'))

            # Check if the dark image exists
            if not os.path.exists(dark_image_file):
                print(f"Dark mode image missing for: {filename}")
                continue

            # Load the images
            image1 = cv2.imread(light_image_file)
            image2 = cv2.imread(dark_image_file)

            if image1 is None or image2 is None:
                print(f"Error loading images: {light_image_file} or {dark_image_file}")
                continue

            # Concatenate images horizontally
            side_by_side = np.hstack((image1, image2))


            # Save the combined image
            cv2.imwrite(output_image_path, side_by_side)
            print(f"Saved combined image: {output_image_path}")



# Define input and output directories
image_dir = 'path/to/input/image/org_size'
output_dir = 'path/to/input/image/lightdark'

# Run the batch process
combine_image = get_image_side_by_side(image_dir, output_dir)
print("Batch Results:", combine_image)
