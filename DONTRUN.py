from PIL import Image
import numpy as np
import random
import os
import concurrent.futures
import time
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
def generate_image(image_index, width, height, base_dir):
    array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    img = Image.fromarray(array, 'RGB')
    folder_name = f'folder{image_index}'
    folder_path = os.path.join(base_dir, folder_name)
    create_directory(folder_path)
    filename = f'large_image_{image_index}.bmp'
    file_path = os.path.join(folder_path, filename)
    img.save(file_path)
    print(f'Generated and saved {file_path} with dimensions {width}x{height}')
def main():
    num_images = 1700
    width, height = 8000, 8000
    base_dir = "generated_images"
    create_directory(base_dir)
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(generate_image, i, width, height, base_dir) for i in range(1, num_images + 1)]
        concurrent.futures.wait(futures)
    end_time = time.time()
    print(f'Finished generating {num_images} images in {end_time - start_time:.2f} seconds')
if __name__ == "__main__":
    main()