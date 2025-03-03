'''
resize the image to [369, 800] as the uied detection resize our org image
'''



import cv2
import os

input_folder = "path/to/input/image/org_size" #input
output_folder = "path/to/input/image/uied_size"  # Folder to save results

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the folder
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Add more extensions if needed
        # Read the image
        image_path = os.path.join(input_folder, filename)
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at path:{image_path}")
        image = cv2.imread(image_path)

        # risize the screenshot to uied size
        resized_image = cv2.resize(image, (369, 800))

        # Save the resized image in the output folder
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, resized_image)

        print(f'Resized and saved: {output_path}')

print("Resizing complete.")