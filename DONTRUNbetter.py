from PIL import Image
import numpy as np
import random
import os
import concurrent.futures
import time

# Function to create a directory
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Function to generate and save the image with random pixels
def generate_image(image_index, width, height, base_dir):
    # Create an array of random colors
    array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

    # Convert the numpy array to a PIL Image
    img = Image.fromarray(array, 'RGB')

    # Create a folder for the image
    folder_name = f'folder{image_index}'
    folder_path = "generated_images"
    create_directory(folder_path)

    # Save the image as a BMP file
    filename = f'large_image_{image_index}.bmp'
    file_path = os.path.join(folder_path, filename)
    img.save(file_path)

    # Print confirmation message (optional)
    print(f'Generated and saved {file_path} with dimensions {width}x{height}')

# Main function to manage image generation
def main():
    # Number of images and their dimensions
    num_images = 1700
    width, height = 8000, 8000

    # Base directory for saving images
    base_dir = "generated_images"
    create_directory(base_dir)

    # Measure the start time
    start_time = time.time()

    # Use ThreadPoolExecutor for concurrent image generation
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(generate_image, i, width, height, base_dir) for i in range(1, num_images + 1)]
        concurrent.futures.wait(futures)

    # Measure the end time
    end_time = time.time()
    print(f'Finished generating {num_images} images in {end_time - start_time:.2f} seconds')

# Run the main function
if __name__ == "__main__":
    main()
