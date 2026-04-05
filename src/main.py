# %% [markdown]
# # dataset load

# %%
import os
import cv2
import numpy as np

def load_data(data_dir):
    images = []
    labels = []
    for main_folder in os.listdir(data_dir):
        main_folder_path = os.path.join(data_dir, main_folder)
        if os.path.isdir(main_folder_path):  # Check if it is a directory
            print(f"Accessing folder: {main_folder_path}")
            for class_name in os.listdir(main_folder_path):
                class_path = os.path.join(main_folder_path, class_name)
                if os.path.isdir(class_path):  # Check if it is a directory
                    print(f"  Accessing class folder: {class_path}")
                    for img_name in os.listdir(class_path):
                        img_path = os.path.join(class_path, img_name)
                        if os.path.isfile(img_path):  # Check if it is a file
                            print(f"    Attempting to load image: {img_path}")
                            img = cv2.imread(img_path)
                            if img is not None:  # Check if the image was loaded successfully
                                img = cv2.resize(img, (256, 256))  # Resize to a fixed size
                                images.append(img)
                                labels.append(class_name)
                            else:
                                print(f"Warning: Failed to load image {img_path}")
    return np.array(images), np.array(labels)

train_dir = "D:\\new maize wheat\\train\\train"
test_dir = "D:\\new maize wheat\\test"
train_images, train_labels = load_data(train_dir)
test_images, test_labels = load_data(test_dir)

# Print shape to confirm resizing
print("Train images shape:", train_images.shape)
print("Test images shape:", test_images.shape)


# %%
import os
import cv2
import numpy as np

def load_data(data_dir):
    images = []
    labels = []
    for root, dirs, files in os.walk(data_dir):
        for img_name in files:
            if img_name.endswith('.jpg') or img_name.endswith('.png'):  # Adjust based on your file types
                img_path = os.path.join(root, img_name)
                img = cv2.imread(img_path)
                img = cv2.resize(img, (256, 256))  # Resize to a fixed size
                images.append(img)
                # Use the last part of the path as the label (folder name indicating the disease)
                labels.append(os.path.basename(os.path.dirname(img_path)))
    return np.array(images), np.array(labels)

train_dir = "D:\\new maize wheat\\train\\train"
test_dir = "D:\\new maize wheat\\test\\test"
train_images, train_labels = load_data(train_dir)
test_images, test_labels = load_data(test_dir)


# %%
pip install Pillow


# %%
import os
from PIL import Image

# Define a set of valid image extensions including .jfif
VALID_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jfif'}

def is_image_file(filename):
    """Check if the file is a valid image based on its extension."""
    return any(filename.lower().endswith(ext) for ext in VALID_IMAGE_EXTENSIONS)

def process_images_in_directory(directory):
    """Process all images in the specified directory and its subdirectories."""
    for dirpath, dirnames, filenames in os.walk(directory):
        print(f"Checking directory: {dirpath}")
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if is_image_file(filename):
                try:
                    with Image.open(file_path) as img:
                        # Process the image (e.g., print size, show, etc.)
                        print(f"Processing file: {filename} (Size: {img.size})")
                except Exception as e:
                    print(f"Error processing file: {filename}, Error: {e}")
            else:
                print(f"Skipping file: {filename}, not an image")

# Replace with your actual train directory path
train_directory = r"D:\new maize wheat\train\train"
process_images_in_directory(train_directory)

# Replace with your actual test directory path
test_directory = r"D:\new maize wheat\test\test"
process_images_in_directory(test_directory)


# %%
import os
from PIL import Image
import numpy as np

# Define a set of valid image extensions including .jfif
VALID_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jfif'}

def is_image_file(filename):
    """Check if the file is a valid image based on its extension."""
    return any(filename.lower().endswith(ext) for ext in VALID_IMAGE_EXTENSIONS)

def normalize_and_resize_image(img, target_size=(224, 224)):
    """Normalize and resize the image."""
    # Resize the image
    img = img.resize(target_size)

    # Convert to numpy array and normalize pixel values to range [0, 1]
    img_array = np.array(img) / 255.0

    return img_array

def process_images_in_directory(directory):
    """Process all images in the specified directory and its subdirectories."""
    for dirpath, dirnames, filenames in os.walk(directory):
        print(f"Checking directory: {dirpath}")
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if is_image_file(filename):
                try:
                    with Image.open(file_path) as img:
                        # Normalize and resize the image
                        normalized_image = normalize_and_resize_image(img)

                        # You can save the processed image or use it as needed
                        print(f"Processed file: {filename} (Size: {normalized_image.shape})")
                except Exception as e:
                    print(f"Error processing file: {filename}, Error: {e}")
            else:
                print(f"Skipping file: {filename}, not an image")

# Replace with your actual train directory path
train_directory = r"D:\new maize wheat\train\train"
process_images_in_directory(train_directory)

# Replace with your actual test directory path
test_directory = r"D:\new maize wheat\test\test"
process_images_in_directory(test_directory)


# %%
import os
from PIL import Image
import numpy as np

# Define a set of valid image extensions including .jfif
VALID_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jfif'}

def is_image_file(filename):
    """Check if the file is a valid image based on its extension."""
    return any(filename.lower().endswith(ext) for ext in VALID_IMAGE_EXTENSIONS)

def normalize_and_resize_image(img, target_size=(224, 224)):
    """Normalize and resize the image."""
    # Resize the image
    img = img.resize(target_size)

    # Convert to numpy array and normalize pixel values to range [0, 1]
    img_array = np.array(img) / 255.0

    return img, img_array  # Return both the PIL image and the normalized array

def process_images_in_directory(directory, save_directory):
    """Process all images in the specified directory and its subdirectories."""
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)  # Create save directory if it doesn't exist
    
    for dirpath, dirnames, filenames in os.walk(directory):
        print(f"Checking directory: {dirpath}")
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if is_image_file(filename):
                try:
                    with Image.open(file_path) as img:
                        # Normalize and resize the image
                        resized_image, normalized_image = normalize_and_resize_image(img)

                        # Save the processed image to the specified save directory
                        save_path = os.path.join(save_directory, filename)
                        resized_image.save(save_path)
                        
                        print(f"Processed and saved file: {filename} (Size: {normalized_image.shape})")
                except Exception as e:
                    print(f"Error processing file: {filename}, Error: {e}")
            else:
                print(f"Skipping file: {filename}, not an image")

# Replace with your actual train directory path
train_directory = r"D:\new maize wheat\train\train"
# Define where to save the processed train images
train_save_directory = r"D:\new maize wheat\train\processed"
process_images_in_directory(train_directory, train_save_directory)

# Replace with your actual test directory path
test_directory = r"D:\new maize wheat\test\test"
# Define where to save the processed test images
test_save_directory = r"D:\new maize wheat\test\processed"
process_images_in_directory(test_directory, test_save_directory)


# %%
import os
from PIL import Image
import numpy as np

# Define a set of valid image extensions including .jfif
VALID_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jfif'}

def is_image_file(filename):
    """Check if the file is a valid image based on its extension."""
    return any(filename.lower().endswith(ext) for ext in VALID_IMAGE_EXTENSIONS)

def normalize_and_resize_image(img, target_size=(224, 224)):
    """Normalize and resize the image."""
    # Resize the image
    img = img.resize(target_size)

    # Convert to numpy array and normalize pixel values to range [0, 1]
    img_array = np.array(img) / 255.0

    return img, img_array  # Return both the PIL image and the normalized array

def process_images_in_directory(directory, save_directory):
    """Process all images in the specified directory and its subdirectories."""
    for dirpath, dirnames, filenames in os.walk(directory):
        print(f"Checking directory: {dirpath}")
        # Create the corresponding subdirectory in the save directory
        relative_path = os.path.relpath(dirpath, directory)  # Get the relative path
        save_subdirectory = os.path.join(save_directory, relative_path)  # Create the save path
        os.makedirs(save_subdirectory, exist_ok=True)  # Create the directory if it doesn't exist

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if is_image_file(filename):
                try:
                    with Image.open(file_path) as img:
                        # Normalize and resize the image
                        resized_image, normalized_image = normalize_and_resize_image(img)

                        # Save the processed image to the corresponding subdirectory
                        save_path = os.path.join(save_subdirectory, filename)
                        resized_image.save(save_path)
                        
                        print(f"Processed and saved file: {filename} (Size: {normalized_image.shape}) in {save_subdirectory}")
                except Exception as e:
                    print(f"Error processing file: {filename}, Error: {e}")
            else:
                print(f"Skipping file: {filename}, not an image")

# Replace with your actual train directory path
train_directory = r"D:\new maize wheat\train\train"
# Define where to save the processed train images
train_save_directory = r"D:\new maize wheat\train\processed"
process_images_in_directory(train_directory, train_save_directory)

# Replace with your actual test directory path
test_directory = r"D:\new maize wheat\test\test"
# Define where to save the processed test images
test_save_directory = r"D:\new maize wheat\test\processed"
process_images_in_directory(test_directory, test_save_directory)


# %%
import os
from PIL import Image
import numpy as np

# Define a set of valid image extensions including .jfif
VALID_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jfif'}

def is_image_file(filename):
    """Check if the file is a valid image based on its extension."""
    return any(filename.lower().endswith(ext) for ext in VALID_IMAGE_EXTENSIONS)

def normalize_and_resize_image(img, target_size=(224, 224)):
    """Normalize and resize the image."""
    # Resize the image
    img = img.resize(target_size)

    # Convert to numpy array and normalize pixel values to range [0, 1]
    img_array = np.array(img) / 255.0

    return img, img_array  # Return both the PIL image and the normalized array

def convert_to_hsv(img):
    """Convert the PIL image to HSV color space."""
    # Convert the image to HSV color space
    hsv_image = img.convert('HSV')
    return np.array(hsv_image)  # Return the HSV image as a numpy array

def convert_hsv_to_rgb(hsv_image):
    """Convert an HSV image back to RGB color space."""
    # Convert the numpy array back to a PIL image
    hsv_pil_image = Image.fromarray(hsv_image, 'HSV')
    # Convert the HSV PIL image back to RGB
    rgb_image = hsv_pil_image.convert('RGB')
    return rgb_image

def process_images_in_directory(directory, save_directory):
    """Process all images in the specified directory and its subdirectories."""
    for dirpath, dirnames, filenames in os.walk(directory):
        print(f"Checking directory: {dirpath}")
        # Create the corresponding subdirectory in the save directory
        relative_path = os.path.relpath(dirpath, directory)  # Get the relative path
        save_subdirectory = os.path.join(save_directory, relative_path)  # Create the save path
        os.makedirs(save_subdirectory, exist_ok=True)  # Create the directory if it doesn't exist

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if is_image_file(filename):
                try:
                    with Image.open(file_path) as img:
                        # Normalize and resize the image
                        resized_image, normalized_image = normalize_and_resize_image(img)

                        # Convert the resized image to HSV
                        hsv_image = convert_to_hsv(resized_image)

                        # Convert back to RGB before saving
                        rgb_image = convert_hsv_to_rgb(hsv_image)

                        # Save the processed RGB image to the corresponding subdirectory
                        save_path = os.path.join(save_subdirectory, filename)
                        rgb_image.save(save_path)  # Save as RGB
                        
                        print(f"Processed and saved file: {filename} (RGB Size: {rgb_image.size}) in {save_subdirectory}")
                except Exception as e:
                    print(f"Error processing file: {filename}, Error: {e}")
            else:
                print(f"Skipping file: {filename}, not an image")

# Replace with your actual train directory path
train_directory = r"D:\new maize wheat\train\processed"
# Define where to save the processed train images
train_save_directory = r"D:\new maize wheat\train\processed\hsv"
process_images_in_directory(train_directory, train_save_directory)

# Replace with your actual test directory path
test_directory = r"D:\new maize wheat\test\processed"
# Define where to save the processed test images
test_save_directory = r"D:\new maize wheat\test\processed\hsv"
process_images_in_directory(test_directory, test_save_directory)


# %%
import os
from PIL import Image

# Define a set of valid image extensions including .jfif
VALID_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jfif'}

def is_image_file(filename):
    """Check if the file is a valid image based on its extension."""
    return any(filename.lower().endswith(ext) for ext in VALID_IMAGE_EXTENSIONS)

def convert_image_to_jpg(input_path, output_path):
    """Convert an image to JPG format."""
    with Image.open(input_path) as img:
        # Convert the image to RGB (in case it's in a different color mode)
        rgb_image = img.convert('RGB')
        # Save the image in JPG format
        rgb_image.save(output_path, 'JPEG')

def process_images_in_directory(input_directory, output_directory):
    """Process all images in the specified directory and its subdirectories."""
    for dirpath, dirnames, filenames in os.walk(input_directory):
        print(f"Checking directory: {dirpath}")
        # Create the corresponding subdirectory in the output directory
        relative_path = os.path.relpath(dirpath, input_directory)
        output_subdirectory = os.path.join(output_directory, relative_path)
        os.makedirs(output_subdirectory, exist_ok=True)

        for filename in filenames:
            input_file_path = os.path.join(dirpath, filename)
            if is_image_file(filename):
                try:
                    # Define the output file path with .jpg extension
                    output_file_name = os.path.splitext(filename)[0] + '.jpg'
                    output_file_path = os.path.join(output_subdirectory, output_file_name)

                    # Convert the image to JPG format
                    convert_image_to_jpg(input_file_path, output_file_path)

                    print(f"Converted and saved file: {output_file_name} in {output_subdirectory}")
                except Exception as e:
                    print(f"Error processing file: {filename}, Error: {e}")
            else:
                print(f"Skipping file: {filename}, not an image")

# Replace with your actual input directory path
input_directory = r"D:\new maize wheat\test\processed"
# Replace with your desired output directory path
output_directory = r"D:\new maize wheat\test\processed\jpg"
process_images_in_directory(input_directory, output_directory)


# %%
import os
from PIL import Image
import numpy as np

# Define a set of valid image extensions including .jfif
VALID_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jfif'}

def is_image_file(filename):
    """Check if the file is a valid image based on its extension."""
    return any(filename.lower().endswith(ext) for ext in VALID_IMAGE_EXTENSIONS)

def normalize_and_resize_image(img, target_size=(224, 224)):
    """Normalize and resize the image."""
    # Resize the image
    img = img.resize(target_size)

    # Convert to numpy array and normalize pixel values to range [0, 1]
    img_array = np.array(img) / 255.0

    return img, img_array  # Return both the PIL image and the normalized array

def convert_to_hsv(img):
    """Convert the PIL image to HSV color space."""
    # Convert the image to HSV color space
    hsv_image = img.convert('HSV')
    return np.array(hsv_image)  # Return the HSV image as a numpy array

def process_images_in_directory(input_directory, output_directory):
    """Process all images in the specified directory and its subdirectories."""
    for dirpath, dirnames, filenames in os.walk(input_directory):
        print(f"Checking directory: {dirpath}")
        # Create the corresponding subdirectory in the output directory
        relative_path = os.path.relpath(dirpath, input_directory)
        output_subdirectory = os.path.join(output_directory, relative_path)
        os.makedirs(output_subdirectory, exist_ok=True)

        for filename in filenames:
            input_file_path = os.path.join(dirpath, filename)
            if is_image_file(filename):
                try:
                    with Image.open(input_file_path) as img:
                        # Normalize and resize the image
                        resized_image, _ = normalize_and_resize_image(img)

                        # Convert the resized image to HSV
                        hsv_image = convert_to_hsv(resized_image)

                        # Save the processed HSV image to the corresponding subdirectory
                        output_file_name = os.path.splitext(filename)[0] + '_hsv.jpg'
                        output_file_path = os.path.join(output_subdirectory, output_file_name)
                        
                        # Convert the HSV array back to a PIL image for saving
                        hsv_pil_image = Image.fromarray(hsv_image, 'HSV').convert('RGB')  # Convert back to RGB to save as JPG
                        hsv_pil_image.save(output_file_path, 'JPEG')
                        
                        print(f"Processed and saved file: {output_file_name} in {output_subdirectory}")
                except Exception as e:
                    print(f"Error processing file: {filename}, Error: {e}")
            else:
                print(f"Skipping file: {filename}, not an image")

# Replace with your actual input directory path
input_directory = r"D:\new maize wheat\test\jpg"
# Replace with your desired output directory path
output_directory = r"D:\new maize wheat\test\hsv"
process_images_in_directory(input_directory, output_directory)


# %%


# %%
import os
from PIL import Image
import numpy as np

# Define a set of valid image extensions including .jfif
VALID_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jfif'}

def is_image_file(filename):
    """Check if the file is a valid image based on its extension."""
    return any(filename.lower().endswith(ext) for ext in VALID_IMAGE_EXTENSIONS)

def normalize_and_resize_image(img, target_size=(224, 224)):
    """Normalize and resize the image."""
    # Resize the image
    img = img.resize(target_size)

    # Convert to numpy array and normalize pixel values to range [0, 1]
    img_array = np.array(img) / 255.0

    return img, img_array  # Return both the PIL image and the normalized array

def convert_to_hsv(img):
    """Convert the PIL image to HSV color space."""
    # Convert the image to HSV color space
    hsv_image = img.convert('HSV')
    return np.array(hsv_image)  # Return the HSV image as a numpy array

def calculate_average_hsv(hsv_image):
    """Calculate the average HSV values of the image."""
    # Calculate the mean of each channel in the HSV image
    h_mean = np.mean(hsv_image[:, :, 0])  # Hue channel
    s_mean = np.mean(hsv_image[:, :, 1])  # Saturation channel
    v_mean = np.mean(hsv_image[:, :, 2])  # Value channel
    return h_mean, s_mean, v_mean

def process_images_in_directory(input_directory, output_directory):
    """Process all images in the specified directory and its subdirectories."""
    for dirpath, dirnames, filenames in os.walk(input_directory):
        print(f"Checking directory: {dirpath}")
        # Create the corresponding subdirectory in the output directory
        relative_path = os.path.relpath(dirpath, input_directory)
        output_subdirectory = os.path.join(output_directory, relative_path)
        os.makedirs(output_subdirectory, exist_ok=True)

        for filename in filenames:
            input_file_path = os.path.join(dirpath, filename)
            if is_image_file(filename):
                try:
                    with Image.open(input_file_path) as img:
                        # Normalize and resize the image
                        resized_image, _ = normalize_and_resize_image(img)

                        # Convert the resized image to HSV
                        hsv_image = convert_to_hsv(resized_image)

                        # Calculate the average HSV values
                        h_mean, s_mean, v_mean = calculate_average_hsv(hsv_image)

                        # Save the processed HSV image to the corresponding subdirectory
                        output_file_name = os.path.splitext(filename)[0] + '_hsv.jpg'
                        output_file_path = os.path.join(output_subdirectory, output_file_name)
                        
                        # Convert the HSV array back to a PIL image for saving
                        hsv_pil_image = Image.fromarray(hsv_image, 'HSV').convert('RGB')  # Convert back to RGB to save as JPG
                        hsv_pil_image.save(output_file_path, 'JPEG')
                        
                        # Print the average HSV values
                        print(f"Processed and saved file: {output_file_name} in {output_subdirectory}")
                        print(f"Average HSV values for {output_file_name}: H={h_mean:.2f}, S={s_mean:.2f}, V={v_mean:.2f}")
                except Exception as e:
                    print(f"Error processing file: {filename}, Error: {e}")
            else:
                print(f"Skipping file: {filename}, not an image")

# Replace with your actual input directory path
input_directory = r"D:\new maize wheat\test\jpg"
# Replace with your desired output directory path
output_directory = r"D:\new maize wheat\test\hsv"
process_images_in_directory(input_directory, output_directory)


# %%
import os
from PIL import Image
import numpy as np

# Define a set of valid image extensions including .jfif
VALID_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jfif'}

def is_image_file(filename):
    """Check if the file is a valid image based on its extension."""
    return any(filename.lower().endswith(ext) for ext in VALID_IMAGE_EXTENSIONS)

def normalize_and_resize_image(img, target_size=(224, 224)):
    """Normalize and resize the image."""
    # Resize the image
    img = img.resize(target_size)

    # Convert to numpy array and normalize pixel values to range [0, 1]
    img_array = np.array(img) / 255.0

    return img, img_array  # Return both the PIL image and the normalized array

def convert_to_hsv(img):
    """Convert the PIL image to HSV color space."""
    # Convert the image to HSV color space
    hsv_image = img.convert('HSV')
    return np.array(hsv_image)  # Return the HSV image as a numpy array

def calculate_average_hsv(hsv_image):
    """Calculate the average HSV values of the image."""
    # Calculate the mean of each channel in the HSV image
    h_mean = np.mean(hsv_image[:, :, 0])  # Hue channel
    s_mean = np.mean(hsv_image[:, :, 1])  # Saturation channel
    v_mean = np.mean(hsv_image[:, :, 2])  # Value channel
    return h_mean, s_mean, v_mean

def process_images_in_directory(input_directory, output_directory):
    """Process all images in the specified directory and its subdirectories."""
    for dirpath, dirnames, filenames in os.walk(input_directory):
        print(f"Checking directory: {dirpath}")
        # Create the corresponding subdirectory in the output directory
        relative_path = os.path.relpath(dirpath, input_directory)
        output_subdirectory = os.path.join(output_directory, relative_path)
        os.makedirs(output_subdirectory, exist_ok=True)

        for filename in filenames:
            input_file_path = os.path.join(dirpath, filename)
            if is_image_file(filename):
                try:
                    with Image.open(input_file_path) as img:
                        # Normalize and resize the image
                        resized_image, _ = normalize_and_resize_image(img)

                        # Convert the resized image to HSV
                        hsv_image = convert_to_hsv(resized_image)

                        # Calculate the average HSV values
                        h_mean, s_mean, v_mean = calculate_average_hsv(hsv_image)

                        # Save the processed HSV image to the corresponding subdirectory
                        output_file_name = os.path.splitext(filename)[0] + '_hsv.jpg'
                        output_file_path = os.path.join(output_subdirectory, output_file_name)
                        
                        # Convert the HSV array back to a PIL image for saving
                        hsv_pil_image = Image.fromarray(hsv_image, 'HSV').convert('RGB')  # Convert back to RGB to save as JPG
                        hsv_pil_image.save(output_file_path, 'JPEG')
                        
                        # Print the average HSV values
                        print(f"Processed and saved file: {output_file_name} in {output_subdirectory}")
                        print(f"Average HSV values for {output_file_name}: H={h_mean:.2f}, S={s_mean:.2f}, V={v_mean:.2f}")
                except Exception as e:
                    print(f"Error processing file: {filename}, Error: {e}")
            else:
                print(f"Skipping file: {filename}, not an image")

# Replace with your actual input directory path
input_directory = r"D:\new maize wheat\train\jpg"
# Replace with your desired output directory path
output_directory = r"D:\new maize wheat\train\hsv"
process_images_in_directory(input_directory, output_directory)


# %%
pip install matplotlib


# %%
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Define a set of valid image extensions including .jfif
VALID_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jfif'}

def is_image_file(filename):
    """Check if the file is a valid image based on its extension."""
    return any(filename.lower().endswith(ext) for ext in VALID_IMAGE_EXTENSIONS)

def normalize_and_resize_image(img, target_size=(224, 224)):
    """Normalize and resize the image."""
    # Resize the image
    img = img.resize(target_size)

    # Convert to numpy array and normalize pixel values to range [0, 1]
    img_array = np.array(img) / 255.0

    return img, img_array  # Return both the PIL image and the normalized array

def convert_to_hsv(img):
    """Convert the PIL image to HSV color space."""
    # Convert the image to HSV color space
    hsv_image = img.convert('HSV')
    return np.array(hsv_image)  # Return the HSV image as a numpy array

def process_images_in_directory(input_directory, output_directory):
    """Process all images in the specified directory and its subdirectories."""
    folder_visualized = set()  # Track folders from which images have been visualized
    for dirpath, dirnames, filenames in os.walk(input_directory):
        print(f"Checking directory: {dirpath}")
        # Create the corresponding subdirectory in the output directory
        relative_path = os.path.relpath(dirpath, input_directory)
        output_subdirectory = os.path.join(output_directory, relative_path)
        os.makedirs(output_subdirectory, exist_ok=True)

        for filename in filenames:
            input_file_path = os.path.join(dirpath, filename)
            if is_image_file(filename):
                try:
                    with Image.open(input_file_path) as img:
                        # Normalize and resize the image
                        resized_image, _ = normalize_and_resize_image(img)

                        # Convert the resized image to HSV
                        hsv_image = convert_to_hsv(resized_image)

                        # Save the processed HSV image to the corresponding subdirectory
                        output_file_name = os.path.splitext(filename)[0] + '_hsv.jpg'
                        output_file_path = os.path.join(output_subdirectory, output_file_name)
                        
                        # Convert the HSV array back to a PIL image for saving
                        hsv_pil_image = Image.fromarray(hsv_image, 'HSV').convert('RGB')  # Convert back to RGB to save as JPG
                        hsv_pil_image.save(output_file_path, 'JPEG')
                        
                        # Visualize the original and HSV images for one image per folder
                        if relative_path not in folder_visualized:
                            visualize_images(resized_image, hsv_image, filename, relative_path)
                            folder_visualized.add(relative_path)
                            
                        print(f"Processed and saved file: {output_file_name} in {output_subdirectory}")
                except Exception as e:
                    print(f"Error processing file: {filename}, Error: {e}")
            else:
                print(f"Skipping file: {filename}, not an image")

def visualize_images(original_image, hsv_image, filename, relative_path):
    """Visualize the original and HSV images side by side."""
    # Create a figure to display the images
    plt.figure(figsize=(12, 6))

    # Original Image
    plt.subplot(1, 2, 1)
    plt.imshow(original_image)
    plt.title(f'Original Image: {filename}')
    plt.axis('off')

    # HSV Image
    plt.subplot(1, 2, 2)
    plt.imshow(hsv_image)
    plt.title(f'HSV Image: {filename}')
    plt.axis('off')

    # Show the plot
    plt.suptitle(f'Images from: {relative_path}')
    plt.show()

# Replace with your actual input directory path
input_directory = r"D:\new maize wheat\train\jpg"
# Replace with your desired output directory path
output_directory = r"D:\new maize wheat\train\hsv"
process_images_in_directory(input_directory, output_directory)


# %%
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def load_and_convert_images_to_hsv(directory):
    """Load images from a directory and convert them to HSV."""
    hsv_images = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.jfif', '.bmp', '.gif')):
                try:
                    img = Image.open(file_path).convert('RGB')  # Open and convert to RGB
                    img_array = np.array(img)
                    hsv_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)  # Convert to HSV
                    hsv_images.append(hsv_img)
                except Exception as e:
                    print(f"Error loading image {file_path}: {e}")
    return hsv_images

def extract_hsv_features(images):
    """Extract HSV features from a list of HSV images."""
    hsv_features = []
    for hsv_img in images:
        hist_h = cv2.calcHist([hsv_img], [0], None, [256], [0, 256])  # Hue
        hist_s = cv2.calcHist([hsv_img], [1], None, [256], [0, 256])  # Saturation
        hist_v = cv2.calcHist([hsv_img], [2], None, [256], [0, 256])  # Value
        hsv_features.append(np.concatenate([hist_h.flatten(), hist_s.flatten(), hist_v.flatten()]))
    return np.array(hsv_features)

def visualize_hsv_features(hsv_images):
    """Visualize the HSV histograms for the given images."""
    for i, hsv_img in enumerate(hsv_images):
        plt.figure(figsize=(12, 6))
        
        # Calculate histograms
        hist_h = cv2.calcHist([hsv_img], [0], None, [256], [0, 256])  # Hue
        hist_s = cv2.calcHist([hsv_img], [1], None, [256], [0, 256])  # Saturation
        hist_v = cv2.calcHist([hsv_img], [2], None, [256], [0, 256])  # Value
        
        # Plot histograms
        plt.subplot(1, 3, 1)
        plt.plot(hist_h, color='r')
        plt.title('Hue Histogram')
        plt.xlim([0, 256])

        plt.subplot(1, 3, 2)
        plt.plot(hist_s, color='g')
        plt.title('Saturation Histogram')
        plt.xlim([0, 256])

        plt.subplot(1, 3, 3)
        plt.plot(hist_v, color='b')
        plt.title('Value Histogram')
        plt.xlim([0, 256])

        plt.suptitle(f'Image {i + 1} HSV Features')
        plt.show()

# Replace with your actual train and test directory paths
train_directory = r"D:\new maize wheat\train\hsv"  # Update this path
test_directory = r"D:\new maize wheat\test\hsv"    # Update this path

# Load and convert images from the directories to HSV
train_hsv_images = load_and_convert_images_to_hsv(train_directory)
test_hsv_images = load_and_convert_images_to_hsv(test_directory)

# Extract HSV features
train_hsv_features = extract_hsv_features(train_hsv_images)
test_hsv_features = extract_hsv_features(test_hsv_images)

# Output the shape of the extracted features for verification
print(f"Train HSV Features Shape: {train_hsv_features.shape}")
print(f"Test HSV Features Shape: {test_hsv_features.shape}")

# Visualize the HSV features for at least one image from each folder
if train_hsv_images:
    visualize_hsv_features(train_hsv_images[:1])  # Visualize the first image from train set
if test_hsv_images:
    visualize_hsv_features(test_hsv_images[:1])  # Visualize the first image from test set


# %%
def visualize_hsv_features(original_images, hsv_images):
    """Visualize the original image and the HSV histograms for the given images."""
    for i, (original_img, hsv_img) in enumerate(zip(original_images, hsv_images)):
        plt.figure(figsize=(15, 6))
        
        # Plot original image
        plt.subplot(1, 4, 1)
        plt.imshow(original_img)
        plt.title('Original Image')
        plt.axis('off')

        # Calculate histograms
        hist_h = cv2.calcHist([hsv_img], [0], None, [256], [0, 256])  # Hue
        hist_s = cv2.calcHist([hsv_img], [1], None, [256], [0, 256])  # Saturation
        hist_v = cv2.calcHist([hsv_img], [2], None, [256], [0, 256])  # Value
        
        # Plot histograms
        plt.subplot(1, 4, 2)
        plt.plot(hist_h, color='r')
        plt.title('Hue Histogram')
        plt.xlim([0, 256])

        plt.subplot(1, 4, 3)
        plt.plot(hist_s, color='g')
        plt.title('Saturation Histogram')
        plt.xlim([0, 256])

        plt.subplot(1, 4, 4)
        plt.plot(hist_v, color='b')
        plt.title('Value Histogram')
        plt.xlim([0, 256])

        plt.suptitle(f'Image {i + 1} HSV Features')
        plt.show()

# Load and convert images from the directories to HSV (this part remains unchanged)
train_hsv_images = load_and_convert_images_to_hsv(train_directory)
test_hsv_images = load_and_convert_images_to_hsv(test_directory)

# Extract HSV features (this part remains unchanged)
train_hsv_features = extract_hsv_features(train_hsv_images)
test_hsv_features = extract_hsv_features(test_hsv_images)

# Visualize the HSV features for at least one image from each folder, including the original image
if train_hsv_images:
    visualize_hsv_features(train_hsv_images[:1], train_hsv_images[:1])  # Visualize the first image from train set
if test_hsv_images:
    visualize_hsv_features(test_hsv_images[:1], test_hsv_images[:1])  # Visualize the first image from test set


# %%


# %%
pip install opencv-python


# %%
import os
import cv2
import numpy as np
from PIL import Image

# Define a function to load images and convert them to HSV
def load_and_convert_images_to_hsv(directory):
    """Load images from a directory and convert them to HSV."""
    hsv_images = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.jfif', '.bmp', '.gif')):
                try:
                    img = Image.open(file_path).convert('RGB')  # Open and convert to RGB
                    img_array = np.array(img)
                    hsv_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)  # Convert to HSV
                    hsv_images.append(hsv_img)
                except Exception as e:
                    print(f"Error loading image {file_path}: {e}")
    return hsv_images

def extract_hsv_features(images):
    """Extract HSV features from a list of HSV images."""
    hsv_features = []
    for hsv_img in images:
        hist_h = cv2.calcHist([hsv_img], [0], None, [256], [0, 256])  # Hue
        hist_s = cv2.calcHist([hsv_img], [1], None, [256], [0, 256])  # Saturation
        hist_v = cv2.calcHist([hsv_img], [2], None, [256], [0, 256])  # Value
        hsv_features.append(np.concatenate([hist_h.flatten(), hist_s.flatten(), hist_v.flatten()]))
    return np.array(hsv_features)

# Replace with your actual train and test directory paths
train_directory = r"D:\new maize wheat\train\hsv"  # Update this path
test_directory = r"D:\new maize wheat\test\hsv"    # Update this path

# Load and convert images from the directories to HSV
train_hsv_images = load_and_convert_images_to_hsv(train_directory)
test_hsv_images = load_and_convert_images_to_hsv(test_directory)

# Extract HSV features
train_hsv_features = extract_hsv_features(train_hsv_images)
test_hsv_features = extract_hsv_features(test_hsv_images)

# Output the shape of the extracted features for verification
print(f"Train HSV Features Shape: {train_hsv_features.shape}")
print(f"Test HSV Features Shape: {test_hsv_features.shape}")


# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import graycomatrix, graycoprops

def extract_texture_features(images):
    texture_features = []
    for img in images:
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        
        # Convert to uint8
        gray_img = (gray_img * 255).astype(np.uint8)  # Ensure it's in the range of 0-255

        # Compute GLCM
        glcm = graycomatrix(gray_img, distances=[1], angles=[0], levels=256, symmetric=True, normed=True)
        
        # Extract features from GLCM
        contrast = graycoprops(glcm, 'contrast')[0, 0]
        dissimilarity = graycoprops(glcm, 'dissimilarity')[0, 0]
        homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]
        
        texture_features.append([contrast, dissimilarity, homogeneity])
    
    return np.array(texture_features)

# Assuming train_images and test_images are defined as your datasets
train_texture_features = extract_texture_features(train_images)
test_texture_features = extract_texture_features(test_images)

# Print the shape of the texture features
print("Train Texture Features Shape:", train_texture_features.shape)
print("Test Texture Features Shape:", test_texture_features.shape)


# %%
import matplotlib.pyplot as plt

# Calculate mean values for each feature
train_mean_features = train_texture_features.mean(axis=0)
test_mean_features = test_texture_features.mean(axis=0)

# Feature names
feature_names = ['Contrast', 'Dissimilarity', 'Homogeneity']

# Bar plot
x = np.arange(len(feature_names))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, train_mean_features, width, label='Train')
bars2 = ax.bar(x + width/2, test_mean_features, width, label='Test')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Mean Value')
ax.set_title('Mean Texture Features for Train and Test Datasets')
ax.set_xticks(x)
ax.set_xticklabels(feature_names)
ax.legend()

# Display the mean values on top of the bars
def add_value_labels(bars):
    """Add labels to the bars in the bar plot."""
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',  # format the value
                    xy=(bar.get_x() + bar.get_width() / 2, height),  # position the label
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",  # how to position the text
                    ha='center', va='bottom')

add_value_labels(bars1)
add_value_labels(bars2)

plt.tight_layout()
plt.show()


# %%
# Assuming train_images contains the same images for both features
# Recalculate the features to ensure they are derived from the same dataset
# You may want to extract features from the same image set

# Re-extract the HSV features from the original training images
train_hsv_features = extract_hsv_features(train_images)
train_texture_features = extract_texture_features(train_images)  # Ensure the same image set

# Similarly for the test set
test_hsv_features = extract_hsv_features(test_images)
test_texture_features = extract_texture_features(test_images)  # Ensure the same image set

# Now combine the features
train_features = np.hstack((train_hsv_features, train_texture_features))
test_features = np.hstack((test_hsv_features, test_texture_features))

# Print the shapes to confirm they match
print("Combined Train Features Shape:", train_features.shape)
print("Combined Test Features Shape:", test_features.shape)


# %%
def plot_scatter(features, title):
    plt.figure(figsize=(10, 7))
    plt.scatter(features[:, 0], features[:, 1], alpha=0.5)
    plt.title(f'{title} - Feature 1 vs Feature 2')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.grid(True)
    plt.show()

# Visualize the scatter plot for training features
plot_scatter(train_features, 'Training Features')

# Visualize the scatter plot for testing features
plot_scatter(test_features, 'Testing Features')


# %%
from sklearn.decomposition import PCA

def plot_pca(features, title):
    pca = PCA(n_components=2)
    reduced_features = pca.fit_transform(features)

    plt.figure(figsize=(10, 7))
    plt.scatter(reduced_features[:, 0], reduced_features[:, 1], alpha=0.5)
    plt.title(f'{title} - PCA of Combined Features')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.grid(True)
    plt.show()

# Visualize PCA for training features
plot_pca(train_features, 'Training Features')

# Visualize PCA for testing features
plot_pca(test_features, 'Testing Features')


# %%
import os
import numpy as np

# Define the path to your training data
train_data_path = "D:\\new maize wheat\\train\\hsv"  # Update with your actual path

# Create an empty list to hold labels
train_labels = []
train_features_combined = []  # or whichever feature set you want to use

# Iterate through each folder in the training data
for label in os.listdir(train_data_path):
    folder_path = os.path.join(train_data_path, label)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            # Assuming your features are stored in train_features_combined
            # Append the corresponding label (e.g., 0 for healthy wheat, 1 for leaf rust, 2 for stem rust)
            train_labels.append(label)  # You may need to convert to numerical labels

# Convert labels to a numpy array
train_labels = np.array(train_labels)

# Encode labels if necessary (e.g., using LabelEncoder)
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
train_labels_encoded = label_encoder.fit_transform(train_labels)


# %%
pip install opencv-python


# %%
import os
import numpy as np
import cv2  # Import OpenCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Define the paths for your training and testing data
train_data_path = "D:\\new maize wheat\\train\\hsv"  # Update with your actual path
test_data_path = "D:\\new maize wheat\\test\\hsv"  # Update with your actual test data path

# Create empty lists to hold labels and features for training
train_labels = []
train_features_combined = []

# Load training data
for label in os.listdir(train_data_path):
    folder_path = os.path.join(train_data_path, label)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            # Read the image using OpenCV
            image_path = os.path.join(folder_path, file_name)
            image = cv2.imread(image_path)  # Load the image
            
            # Ensure the image is loaded properly
            if image is not None:
                # Extract features from the image (e.g., flatten the image for SVM)
                feature = image.flatten()  # Example feature extraction
                train_features_combined.append(feature)  # Append the feature to the list
                train_labels.append(label)  # Append the corresponding label

# Convert features and labels to numpy arrays
train_features_combined = np.array(train_features_combined)
train_labels = np.array(train_labels)

# Encode labels using LabelEncoder
label_encoder = LabelEncoder()
train_labels_encoded = label_encoder.fit_transform(train_labels)

# Initialize the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(train_features_combined, train_labels_encoded)

# Validate the model using the training set
y_train_pred = model.predict(train_features_combined)

# Evaluate the model on the training set
print("Training Accuracy:", accuracy_score(train_labels_encoded, y_train_pred))
print("\nTraining Classification Report:\n", classification_report(train_labels_encoded, y_train_pred))

# Load test data from a single folder and evaluate performance
test_labels = []
test_features_combined = []

# Assuming all test images are in a single folder
test_image_files = os.listdir(test_data_path)

for file_name in test_image_files:
    # Read the image using OpenCV
    image_path = os.path.join(test_data_path, file_name)
    image = cv2.imread(image_path)  # Load the image
    
    # Ensure the image is loaded properly
    if image is not None:
        # Extract features from the image
        feature = image.flatten()  # Example feature extraction
        test_features_combined.append(feature)
        # Add a placeholder label for test images if needed
        test_labels.append("unknown")  # Placeholder label, adjust as needed

# Convert test features and labels to numpy arrays
test_features_combined = np.array(test_features_combined)
test_labels = np.array(test_labels)

# Debugging: Check the shape of test_features_combined
print("Shape of test features:", test_features_combined.shape)

# Ensure that there are test features available before prediction
if test_features_combined.size > 0:
    # Test the model
    y_test_pred = model.predict(test_features_combined)

    # Evaluate the test set
    print("Test Predictions:", label_encoder.inverse_transform(y_test_pred))
else:
    print("No test features available for prediction.")


# %%
import os
import numpy as np
import cv2  # Import OpenCV
from sklearn import svm  # Import SVM from sklearn
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Define the paths for your training and testing data
train_data_path = "D:\\new maize wheat\\train\\hsv"  # Update with your actual path
test_data_path = "D:\\new maize wheat\\test\\hsv"  # Update with your actual test data path

# Create empty lists to hold labels and features for training
train_labels = []
train_features_combined = []

# Load training data
for label in os.listdir(train_data_path):
    folder_path = os.path.join(train_data_path, label)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            # Read the image using OpenCV
            image_path = os.path.join(folder_path, file_name)
            image = cv2.imread(image_path)  # Load the image
            
            # Ensure the image is loaded properly
            if image is not None:
                # Extract features from the image (e.g., flatten the image for SVM)
                feature = image.flatten()  # Example feature extraction
                train_features_combined.append(feature)  # Append the feature to the list
                train_labels.append(label)  # Append the corresponding label

# Convert features and labels to numpy arrays
train_features_combined = np.array(train_features_combined)
train_labels = np.array(train_labels)

# Encode labels using LabelEncoder
label_encoder = LabelEncoder()
train_labels_encoded = label_encoder.fit_transform(train_labels)

# Initialize the SVM model
model = svm.SVC(kernel='linear', random_state=42)  # You can try different kernels like 'rbf', 'poly', etc.

# Train the model
model.fit(train_features_combined, train_labels_encoded)

# Validate the model using the training set
y_train_pred = model.predict(train_features_combined)

# Evaluate the model on the training set
print("Training Accuracy:", accuracy_score(train_labels_encoded, y_train_pred))
print("\nTraining Classification Report:\n", classification_report(train_labels_encoded, y_train_pred))

# Load test data from a single folder and evaluate performance
test_labels = []
test_features_combined = []

# Assuming all test images are in a single folder
test_image_files = os.listdir(test_data_path)

for file_name in test_image_files:
    # Read the image using OpenCV
    image_path = os.path.join(test_data_path, file_name)
    image = cv2.imread(image_path)  # Load the image
    
    # Ensure the image is loaded properly
    if image is not None:
        # Extract features from the image
        feature = image.flatten()  # Example feature extraction
        test_features_combined.append(feature)
        # Add a placeholder label for test images if needed
        test_labels.append("unknown")  # Placeholder label, adjust as needed

# Convert test features and labels to numpy arrays
test_features_combined = np.array(test_features_combined)
test_labels = np.array(test_labels)

# Debugging: Check the shape of test_features_combined
print("Shape of test features:", test_features_combined.shape)

# Ensure that there are test features available before prediction
if test_features_combined.size > 0:
    # Test the model
    y_test_pred = model.predict(test_features_combined)

    # Evaluate the test set
    print("Test Predictions:", label_encoder.inverse_transform(y_test_pred))
else:
    print("No test features available for prediction.")


# %%
import os
import numpy as np
import cv2  # Import OpenCV
from sklearn.neighbors import KNeighborsClassifier  # Import KNN
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Define the paths for your training and testing data
train_data_path = "D:\\new maize wheat\\train\\hsv"  # Update with your actual path
test_data_path = "D:\\new maize wheat\\test\\hsv"  # Update with your actual test data path

# Create empty lists to hold labels and features for training
train_labels = []
train_features_combined = []

# Load training data
for label in os.listdir(train_data_path):
    folder_path = os.path.join(train_data_path, label)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            # Read the image using OpenCV
            image_path = os.path.join(folder_path, file_name)
            image = cv2.imread(image_path)  # Load the image
            
            # Ensure the image is loaded properly
            if image is not None:
                # Extract features from the image (e.g., flatten the image for KNN)
                feature = image.flatten()  # Example feature extraction
                train_features_combined.append(feature)  # Append the feature to the list
                train_labels.append(label)  # Append the corresponding label

# Convert features and labels to numpy arrays
train_features_combined = np.array(train_features_combined)
train_labels = np.array(train_labels)

# Encode labels using LabelEncoder
label_encoder = LabelEncoder()
train_labels_encoded = label_encoder.fit_transform(train_labels)

# Initialize the KNN model
model = KNeighborsClassifier(n_neighbors=5)  # You can adjust the number of neighbors

# Train the model
model.fit(train_features_combined, train_labels_encoded)

# Validate the model using the training set
y_train_pred = model.predict(train_features_combined)

# Evaluate the model on the training set
print("Training Accuracy:", accuracy_score(train_labels_encoded, y_train_pred))
print("\nTraining Classification Report:\n", classification_report(train_labels_encoded, y_train_pred))

# Load test data from a single folder and evaluate performance
test_labels = []
test_features_combined = []

# Assuming all test images are in a single folder
test_image_files = os.listdir(test_data_path)

for file_name in test_image_files:
    # Read the image using OpenCV
    image_path = os.path.join(test_data_path, file_name)
    image = cv2.imread(image_path)  # Load the image
    
    # Ensure the image is loaded properly
    if image is not None:
        # Extract features from the image
        feature = image.flatten()  # Example feature extraction
        test_features_combined.append(feature)

# Convert test features to numpy array
test_features_combined = np.array(test_features_combined)

# Debugging: Check the shape of test_features_combined
print("Shape of test features:", test_features_combined.shape)

# Ensure that there are test features available before prediction
if test_features_combined.size > 0:
    # Test the model
    y_test_pred = model.predict(test_features_combined)

    # Print predictions for test images
    print("Test Predictions:", label_encoder.inverse_transform(y_test_pred))
else:
    print("No test features available for prediction.")

    

# %%
import os
import numpy as np
import cv2  # Import OpenCV
from sklearn.naive_bayes import GaussianNB  # Import Gaussian Naive Bayes
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Define the paths for your training and testing data
train_data_path = "D:\\new maize wheat\\train\\hsv"  # Update with your actual path
test_data_path = "D:\\new maize wheat\\test\\hsv"  # Update with your actual test data path

# Create empty lists to hold labels and features for training
train_labels = []
train_features_combined = []

# Load training data
for label in os.listdir(train_data_path):
    folder_path = os.path.join(train_data_path, label)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            # Read the image using OpenCV
            image_path = os.path.join(folder_path, file_name)
            image = cv2.imread(image_path)  # Load the image
            
            # Ensure the image is loaded properly
            if image is not None:
                # Extract features from the image (e.g., flatten the image for Naive Bayes)
                feature = image.flatten()  # Example feature extraction
                train_features_combined.append(feature)  # Append the feature to the list
                train_labels.append(label)  # Append the corresponding label

# Convert features and labels to numpy arrays
train_features_combined = np.array(train_features_combined)
train_labels = np.array(train_labels)

# Encode labels using LabelEncoder
label_encoder = LabelEncoder()
train_labels_encoded = label_encoder.fit_transform(train_labels)

# Initialize the Naive Bayes model
model = GaussianNB()

# Train the model
model.fit(train_features_combined, train_labels_encoded)

# Validate the model using the training set
y_train_pred = model.predict(train_features_combined)

# Evaluate the model on the training set
print("Training Accuracy:", accuracy_score(train_labels_encoded, y_train_pred))
print("\nTraining Classification Report:\n", classification_report(train_labels_encoded, y_train_pred))

# Load test data from a single folder and evaluate performance
test_labels = []
test_features_combined = []

# Assuming all test images are in a single folder
test_image_files = os.listdir(test_data_path)

for file_name in test_image_files:
    # Read the image using OpenCV
    image_path = os.path.join(test_data_path, file_name)
    image = cv2.imread(image_path)  # Load the image
    
    # Ensure the image is loaded properly
    if image is not None:
        # Extract features from the image
        feature = image.flatten()  # Example feature extraction
        test_features_combined.append(feature)

# Convert test features to numpy array
test_features_combined = np.array(test_features_combined)

# Debugging: Check the shape of test_features_combined
print("Shape of test features:", test_features_combined.shape)

# Ensure that there are test features available before prediction
if test_features_combined.size > 0:
    # Test the model
    y_test_pred = model.predict(test_features_combined)

    # Print predictions for test images
    print("Test Predictions:", label_encoder.inverse_transform(y_test_pred))
else:
    print("No test features available for prediction.")


# %%
# Evaluate the model on the test set
if test_features_combined.size > 0:
    y_test_pred = model.predict(test_features_combined)
    
    # You may not have true labels for the test set, but you can still evaluate the predictions
    # If you do have true labels for a validation set, use them here
    print("Test Predictions:", label_encoder.inverse_transform(y_test_pred))
    
    # If you have true labels for the test dataset
    # print("Test Accuracy:", accuracy_score(true_test_labels, y_test_pred))
    # print("\nTest Classification Report:\n", classification_report(true_test_labels, y_test_pred))
else:
    print("No test features available for prediction.")


# %%
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Assuming you have true test labels available (true_test_labels)
# For the sake of the example, let's assume we use "unknown" as a placeholder for the test labels
# You can replace this with your actual test labels if available
true_test_labels = np.array(["unknown"] * len(test_features_combined))  # Placeholder for demonstration

# Calculate confusion matrix
conf_matrix = confusion_matrix(true_test_labels, label_encoder.inverse_transform(y_test_pred))

# Plot the confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()


# %%
# Plotting sample predictions
num_samples = 5  # Number of samples to display
plt.figure(figsize=(15, 10))

for i in range(num_samples):
    plt.subplot(2, num_samples, i + 1)
    img = cv2.imread(os.path.join(test_data_path, test_image_files[i]))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(f'Predicted: {label_encoder.inverse_transform([y_test_pred[i]])[0]}')
    plt.axis('off')

plt.tight_layout()
plt.show()


# %%
import joblib

# Save the model to a file
model_file_path = 'random_forest_model.pkl'  # Specify the path where you want to save the model
joblib.dump(model, model_file_path)
print(f"Model saved to {model_file_path}")


# %%
# Load the model from the file
loaded_model = joblib.load(model_file_path)
print("Model loaded successfully.")


# %%
import os
import numpy as np
import cv2  # Import OpenCV
import joblib
import random
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Define the paths for your training and testing data
train_data_path = "D:\\new maize wheat\\train\\hsv"  # Update with your actual path
test_data_path = "D:\\new maize wheat\\test\\hsv"  # Update with your actual test data path

# Set image dimensions for resizing
image_width = 128
image_height = 128

# Create empty lists to hold labels and features for training
train_labels = []
train_features_combined = []

# Load training data
for label in os.listdir(train_data_path):
    folder_path = os.path.join(train_data_path, label)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, file_name)
            image = cv2.imread(image_path)
            
            # Ensure the image is loaded properly
            if image is not None:
                # Resize the image to fixed dimensions
                image = cv2.resize(image, (image_width, image_height))
                # Extract features from the image
                feature = image.flatten()  # Flatten the resized image
                train_features_combined.append(feature)
                train_labels.append(label)

# Convert features and labels to numpy arrays
train_features_combined = np.array(train_features_combined)
train_labels = np.array(train_labels)

# Encode labels using LabelEncoder
label_encoder = LabelEncoder()
train_labels_encoded = label_encoder.fit_transform(train_labels)

# Initialize and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(train_features_combined, train_labels_encoded)

# Save the model
model_file_path = 'random_forest_model.pkl'
joblib.dump(model, model_file_path)
print(f"Model saved to {model_file_path}")

# Load the model
loaded_model = joblib.load(model_file_path)
print("Model loaded successfully.")

# Function to load and predict images
def load_and_predict_images(image_folder, model, label_encoder):
    image_files = os.listdir(image_folder)
    random_images = random.sample(image_files, 5)  # Randomly select 5 images

    predictions = []
    
    for image_file in random_images:
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)

        if image is not None:
            # Resize the image to fixed dimensions
            image = cv2.resize(image, (image_width, image_height))
            feature = image.flatten().reshape(1, -1)  # Reshape for prediction
            prediction = model.predict(feature)
            predicted_label = label_encoder.inverse_transform(prediction)[0]
            predictions.append((image_file, predicted_label))

            # Display the image and prediction
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            plt.title(f'Predicted: {predicted_label}')
            plt.axis('off')
            plt.show()

    return predictions

# Test the function on a folder of test images
test_folder_path = "D:\\new maize wheat\\test\\hsv"  # Update with your actual test data path
load_and_predict_images(test_folder_path, loaded_model, label_encoder)


# %%
import os
import numpy as np
import cv2
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Define the paths for your training data
train_data_path = "D:\\new maize wheat\\train\\hsv"  # Update with your actual path

# Create empty lists to hold labels and features for training
train_labels = []
train_features_combined = []

# Load training data
for label in os.listdir(train_data_path):
    folder_path = os.path.join(train_data_path, label)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, file_name)
            image = cv2.imread(image_path)

            if image is not None:
                image = cv2.resize(image, (128, 128))  # Resize to fixed dimensions
                feature = image.flatten()
                train_features_combined.append(feature)
                train_labels.append(label)

# Convert features and labels to numpy arrays
train_features_combined = np.array(train_features_combined)
train_labels = np.array(train_labels)

# Encode labels using LabelEncoder
label_encoder = LabelEncoder()
train_labels_encoded = label_encoder.fit_transform(train_labels)

# Save the label encoder
joblib.dump(label_encoder, 'label_encoder.pkl')
print("Label encoder saved successfully.")

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(train_features_combined, train_labels_encoded)

# Save the model
model_file_path = 'random_forest_model.pkl'
joblib.dump(model, model_file_path)
print(f"Model saved to {model_file_path}")


# %%
# Load the trained model and label encoder
model_file_path = 'random_forest_model.pkl'
loaded_model = joblib.load(model_file_path)
label_encoder = joblib.load('label_encoder.pkl')  # This should work if you saved it earlier

print("Model and label encoder loaded successfully.")


# %%
# Load the trained model and label encoder
model_file_path = 'random_forest_model.pkl'
loaded_model = joblib.load(model_file_path)
label_encoder = joblib.load('label_encoder.pkl')  # Ensure you have this file saved

print("Model and label encoder loaded successfully.")

# Function to predict a single image
def predict_single_image(image_path, model, label_encoder):
    image = cv2.imread(image_path)

    if image is not None:
        image = cv2.resize(image, (128, 128))
        feature = image.flatten().reshape(1, -1)
        prediction = model.predict(feature)
        predicted_label = label_encoder.inverse_transform(prediction)[0]

        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(f'Predicted: {predicted_label}')
        plt.axis('off')
        plt.show()

        return predicted_label
    else:
        print("Image not found or unable to load.")
        return None

# Path to the single image you want to predict
single_image_path = "D:\\maize,wheat\\train\\train\\leaf_rust\\00VVPB.jfif"  # Update with your actual image path
predicted_label = predict_single_image(single_image_path, loaded_model, label_encoder)

print(f"The predicted label for the image is: {predicted_label}")


# %%
# Load the trained model and label encoder
model_file_path = 'random_forest_model.pkl'
loaded_model = joblib.load(model_file_path)
label_encoder = joblib.load('label_encoder.pkl')  # Ensure you have this file saved

print("Model and label encoder loaded successfully.")

# Function to predict a single image
def predict_single_image(image_path, model, label_encoder):
    image = cv2.imread(image_path)

    if image is not None:
        image = cv2.resize(image, (128, 128))
        feature = image.flatten().reshape(1, -1)
        prediction = model.predict(feature)
        predicted_label = label_encoder.inverse_transform(prediction)[0]

        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(f'Predicted: {predicted_label}')
        plt.axis('off')
        plt.show()

        return predicted_label
    else:
        print("Image not found or unable to load.")
        return None

# Path to the single image you want to predict
single_image_path = "D:\\new maize wheat\\train\\train\\stem_rust\\00LAS4.JPG" # Update with your actual image path
predicted_label = predict_single_image(single_image_path, loaded_model, label_encoder)

print(f"The predicted label for the image is: {predicted_label}")


# %%


# %%
# Load the trained model and label encoder
model_file_path = 'random_forest_model.pkl'
loaded_model = joblib.load(model_file_path)
label_encoder = joblib.load('label_encoder.pkl')  # This should work if you saved it earlier

print("Model and label encoder loaded successfully.")

# %%
# Load the trained model and label encoder
model_file_path = 'random_forest_model.pkl'
loaded_model = joblib.load(model_file_path)
label_encoder = joblib.load('label_encoder.pkl')  # Ensure you have this file saved

print("Model and label encoder loaded successfully.")

# Function to predict a single image
def predict_single_image(image_path, model, label_encoder):
    image = cv2.imread(image_path)

    if image is not None:
        image = cv2.resize(image, (128, 128))
        feature = image.flatten().reshape(1, -1)
        prediction = model.predict(feature)
        predicted_label = label_encoder.inverse_transform(prediction)[0]

        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(f'Predicted: {predicted_label}')
        plt.axis('off')
        plt.show()

        return predicted_label
    else:
        print("Image not found or unable to load.")
        return None

# Path to the single image you want to predict
single_image_path = "D:\\new maize wheat\\train\\hsv\\healthy_wheat\\03TD19_hsv.jpg"  # Update with your actual image path
predicted_label = predict_single_image(single_image_path, loaded_model, label_encoder)

print(f"The predicted label for the image is: {predicted_label}")


# %%


# %%
# Load the trained model and label encoder
model_file_path = 'random_forest_model.pkl'
loaded_model = joblib.load(model_file_path)
label_encoder = joblib.load('label_encoder.pkl')  # Ensure you have this file saved

print("Model and label encoder loaded successfully.")

# Function to predict a single image
def predict_single_image(image_path, model, label_encoder):
    image = cv2.imread(image_path)

    if image is not None:
        image = cv2.resize(image, (128, 128))
        feature = image.flatten().reshape(1, -1)
        prediction = model.predict(feature)
        predicted_label = label_encoder.inverse_transform(prediction)[0]

        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(f'Predicted: {predicted_label}')
        plt.axis('off')
        plt.show()

        return predicted_label
    else:
        print("Image not found or unable to load.")
        return None

# Path to the single image you want to predict
single_image_path = "D:\\maize,wheat\\test\\test\\2NB0GZ.jfif"  # Update with your actual image path
predicted_label = predict_single_image(single_image_path, loaded_model, label_encoder)

print(f"The predicted label for the image is: {predicted_label}")


# %%
# Load the trained model and label encoder
model_file_path = 'random_forest_model.pkl'
loaded_model = joblib.load(model_file_path)
label_encoder = joblib.load('label_encoder.pkl')  # Ensure you have this file saved

print("Model and label encoder loaded successfully.")

# Function to predict a single image
def predict_single_image(image_path, model, label_encoder):
    image = cv2.imread(image_path)

    if image is not None:
        image = cv2.resize(image, (128, 128))
        feature = image.flatten().reshape(1, -1)
        prediction = model.predict(feature)
        predicted_label = label_encoder.inverse_transform(prediction)[0]

        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(f'Predicted: {predicted_label}')
        plt.axis('off')
        plt.show()

        return predicted_label
    else:
        print("Image not found or unable to load.")
        return None

# Path to the single image you want to predict
single_image_path = "D:\\maize,wheat\\test\\test\\45HKLN.jpg"  # Update with your actual image path
predicted_label = predict_single_image(single_image_path, loaded_model, label_encoder)

print(f"The predicted label for the image is: {predicted_label}")


# %%
import os
import numpy as np
import cv2  # Import OpenCV
import joblib
import random
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Define the paths for your training and testing data
train_data_path = "D:\\new maize wheat\\train\\hsv"  # Path to training folder containing subfolders
test_data_path = "D:\\new maize wheat\\test\\hsv"  # Path to test images

# Set image dimensions for resizing
image_width = 128
image_height = 128

# Create empty lists to hold labels and features for training
train_labels = []
train_features_combined = []

# Load training data from subfolders
for label in os.listdir(train_data_path):
    folder_path = os.path.join(train_data_path, label)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, file_name)
            image = cv2.imread(image_path)
            
            # Ensure the image is loaded properly
            if image is not None:
                # Resize the image to fixed dimensions
                image = cv2.resize(image, (image_width, image_height))
                # Extract features from the image
                feature = image.flatten()  # Flatten the resized image
                train_features_combined.append(feature)
                train_labels.append(label)
            else:
                print(f"Warning: Could not load image {image_path}")

# Check if any features were collected
if not train_features_combined:
    print("Error: No features were collected. Please check the dataset path and ensure images are valid.")
else:
    print(f"Total training samples: {len(train_features_combined)}")

# Convert features and labels to numpy arrays
train_features_combined = np.array(train_features_combined)
train_labels = np.array(train_labels)

# Encode labels using LabelEncoder
label_encoder = LabelEncoder()
train_labels_encoded = label_encoder.fit_transform(train_labels)

# Initialize and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(train_features_combined, train_labels_encoded)

# Save the model and label encoder
joblib.dump(model, 'random_forest_model.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')

print("Model and label encoder saved successfully.")

# Load the model and label encoder
loaded_model = joblib.load('random_forest_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Function to load and predict a single image
def predict_single_image(image_path, model, label_encoder):
    image = cv2.imread(image_path)
    
    if image is not None:
        # Resize the image to fixed dimensions
        image = cv2.resize(image, (image_width, image_height))
        feature = image.flatten().reshape(1, -1)  # Reshape for prediction
        prediction = model.predict(feature)
        predicted_label = label_encoder.inverse_transform(prediction)[0]
        return predicted_label
    else:
        return None

# Example of predicting a single image
test_image_path = "D:\\maize,wheat\\test\\test\\45HKLN.jpg"   # Update with your actual test image path
predicted_stage = predict_single_image(test_image_path, loaded_model, label_encoder)
print(f"Predicted Stage: {predicted_stage}")

# Function to visualize predictions for multiple images
def visualize_predictions(image_folder, model, label_encoder):
    image_files = os.listdir(image_folder)
    random_images = random.sample(image_files, 5)  # Randomly select 5 images

    for image_file in random_images:
        image_path = os.path.join(image_folder, image_file)
        predicted_stage = predict_single_image(image_path, model, label_encoder)
        
        # Display the image and prediction
        image = cv2.imread(image_path)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(f'Predicted: {predicted_stage}')
        plt.axis('off')
        plt.show()

# Visualize predictions on test images
visualize_predictions(test_data_path, loaded_model, label_encoder)


# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt

def generate_heatmap(image, predictions, alpha=0.5):
    # Resize image to 128x128 for heatmap overlay
    image_resized = cv2.resize(image, (128, 128))
    
    # Create a blank heatmap
    heatmap = np.zeros((128, 128), dtype=np.float32)
    
    # Assuming predictions are probabilities from a model, scale them to the heatmap
    for i in range(128):
        for j in range(128):
            heatmap[i, j] = predictions[i, j]  # Modify this based on how you get predictions
    
    # Normalize the heatmap
    heatmap = cv2.normalize(heatmap, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    heatmap_colored = cv2.applyColorMap(np.uint8(255 * heatmap), cv2.COLORMAP_JET)
    
    # Overlay the heatmap on the original image
    overlay = cv2.addWeighted(heatmap_colored, 0.5, image_resized, 0.5, 0)

    return overlay

# Example usage
image_path = "D:\\maize,wheat\\test\\test\\2NB0GZ.jfif"
image = cv2.imread(image_path)
# Assume predictions are a 128x128 array of predicted probabilities for visualization
predictions = np.random.rand(128, 128)  # Replace with your actual model predictions
heatmap_overlay = generate_heatmap(image, predictions)

plt.imshow(cv2.cvtColor(heatmap_overlay, cv2.COLOR_BGR2RGB))
plt.title('Heat Map Overlay')
plt.axis('off')
plt.show()


# %%
def overlay_prediction(image, predicted_label):
    # Resize the image
    image_resized = cv2.resize(image, (128, 128))
    
    # Convert the label to a string for display
    label_text = f"Predicted: {predicted_label}"
    
    # Put the label on the image
    cv2.putText(image_resized, label_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    return image_resized

# Example usage
image_path =  "D:\\maize,wheat\\test\\test\\2NB0GZ.jfif"
image = cv2.imread(image_path)
predicted_label = 'Mid Stage'  # Replace with your actual prediction
overlayed_image = overlay_prediction(image, predicted_label)

plt.imshow(cv2.cvtColor(overlayed_image, cv2.COLOR_BGR2RGB))
plt.title('Prediction Overlay')
plt.axis('off')
plt.show()


# %%
import cv2
import matplotlib.pyplot as plt

def show_before_after(original_image, processed_image, title='Before and After'):
    # Resize both images for consistency
    original_resized = cv2.resize(original_image, (128, 128))
    processed_resized = cv2.resize(processed_image, (128, 128))
    
    # Create a figure to display the images
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original_resized, cv2.COLOR_BGR2RGB))
    plt.title('Before')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(processed_resized, cv2.COLOR_BGR2RGB))
    plt.title('After')
    plt.axis('off')
    
    plt.suptitle(title)
    plt.show()

# Example usage
original_image_path = "D:\\maize,wheat\\test\\test\\2NB0GZ.jfif"
processed_image_path = "D:\\new maize wheat\\test\\hsv\\2NB0GZ_hsv.jpg"  # After your intervention

# Load the images
original_image = cv2.imread(original_image_path)
processed_image = cv2.imread(processed_image_path)

# Show before and after images
show_before_after(original_image, processed_image, title='Before and After Intervention')


# %%
pip install matplotlib Pillow


# %%
import os
import matplotlib.pyplot as plt
from PIL import Image

# Set the path to your dataset directory
dataset_path = "D:\\new maize wheat\\train\\processed"

# List all folders in the dataset directory
folders = os.listdir(dataset_path)

# Number of images to display from each folder
num_images = 2

# Create a figure for plotting
plt.figure(figsize=(6, 6))

# Loop through each folder and display the first two images
for idx, folder in enumerate(folders):
    folder_path = os.path.join(dataset_path, folder)
    
    # Check if it's a directory
    if os.path.isdir(folder_path):
        # Get all images in the folder
        images = [img for img in os.listdir(folder_path) if img.endswith(('.png', '.jpg', '.jpeg'))]
        
        # Limit to first num_images or available images
        selected_images = images[:num_images]

        for i, image_name in enumerate(selected_images):
            img_path = os.path.join(folder_path, image_name)
            img = Image.open(img_path)

            # Create a subplot for each image
            plt.subplot(len(folders), num_images, idx * num_images + i + 1)
            plt.imshow(img)
            plt.axis('off')
            plt.title(folder)  # Set title as folder name

# Adjust layout
plt.tight_layout()
plt.show()


# %%
import os
import cv2
import matplotlib.pyplot as plt

# Define the path to the dataset folder containing subfolders of images
dataset_path = "D:\\new maize wheat\\train\\hsv"  # Update with your actual path

# Iterate through each folder and process the first image
for folder_name in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder_name)
    if os.path.isdir(folder_path):
        # Get the first image file in the folder
        image_files = os.listdir(folder_path)
        if image_files:
            first_image_path = os.path.join(folder_path, image_files[0])
            image = cv2.imread(first_image_path)
            
            # Convert the image to HSV
            hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            
            # Split the HSV channels
            h_channel, s_channel, v_channel = cv2.split(hsv_image)
            
            # Display the original and HSV channels
            plt.figure(figsize=(6, 6))
            
            plt.subplot(1, 4, 1)
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            plt.title(f'{folder_name} - Original')
            plt.axis('off')
            
            plt.subplot(1, 4, 2)
            plt.imshow(h_channel, cmap='gray')
            plt.title('Hue')
            plt.axis('off')
            
            plt.subplot(1, 4, 3)
            plt.imshow(s_channel, cmap='gray')
            plt.title('Saturation')
            plt.axis('off')
            
            plt.subplot(1, 4, 4)
            plt.imshow(v_channel, cmap='gray')
            plt.title('Value')
            plt.axis('off')
            
            plt.show()


# %%
import os
import matplotlib.pyplot as plt
from PIL import Image

def display_images_in_grid(base_folder, num_images=3):
    folders = [f for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]
    fig, axs = plt.subplots(len(folders), num_images, figsize=(num_images * 3, len(folders) * 3))
    
    for row, folder in enumerate(folders):
        folder_path = os.path.join(base_folder, folder)
        images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))][:num_images]
        
        for col, image_name in enumerate(images):
            image_path = os.path.join(folder_path, image_name)
            image = Image.open(image_path)
            
            axs[row, col].imshow(image)
            axs[row, col].axis('off')
            axs[row, col].set_title(f"{folder} - Image {col+1}")
    
    plt.tight_layout()
    plt.show()

# Specify the path to the base folder containing the subfolders with images
base_folder = "D:\\new maize wheat\\train\\train"
display_images_in_grid(base_folder)


# %%
import os
import matplotlib.pyplot as plt
from PIL import Image

def display_images_in_grid(base_folder, num_images=3):
    folders = [f for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]
    # Reduced figsize for smaller images
    fig, axs = plt.subplots(len(folders), num_images, figsize=(num_images * 2, len(folders) * 2))
    
    for row, folder in enumerate(folders):
        folder_path = os.path.join(base_folder, folder)
        images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))][:num_images]
        
        for col, image_name in enumerate(images):
            image_path = os.path.join(folder_path, image_name)
            image = Image.open(image_path)
            
            axs[row, col].imshow(image)
            axs[row, col].axis('off')
            axs[row, col].set_title(f"{folder} - Image {col+1}")
    
    plt.tight_layout()
    plt.show()

# Specify the path to the base folder containing the subfolders with images
base_folder = "D:\\new maize wheat\\train\\train"
display_images_in_grid(base_folder)


# %%
import cv2
import os
import matplotlib.pyplot as plt
from PIL import Image

def load_and_convert_images_to_hsv(directory):
    """Load images from a directory and convert them to HSV color space."""
    images = []
    for filename in os.listdir(directory):
        img_path = os.path.join(directory, filename)
        if os.path.isfile(img_path):
            img = cv2.imread(img_path)
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            images.append((img, img_hsv))
    return images

def visualize_hsv_features(original_images, hsv_images):
    """Visualize the original image and the HSV histograms for the given images."""
    for i, (original_img, hsv_img) in enumerate(zip(original_images, hsv_images)):
        plt.figure(figsize=(15, 6))
        
        # Plot original image
        plt.subplot(1, 4, 1)
        plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
        plt.title('Original Image')
        plt.axis('off')

        # Calculate histograms
        hist_h = cv2.calcHist([hsv_img], [0], None, [256], [0, 256])  # Hue
        hist_s = cv2.calcHist([hsv_img], [1], None, [256], [0, 256])  # Saturation
        hist_v = cv2.calcHist([hsv_img], [2], None, [256], [0, 256])  # Value
        
        # Plot histograms
        plt.subplot(1, 4, 2)
        plt.plot(hist_h, color='r')
        plt.title('Hue Histogram')
        plt.xlim([0, 256])

        plt.subplot(1, 4, 3)
        plt.plot(hist_s, color='g')
        plt.title('Saturation Histogram')
        plt.xlim([0, 256])

        plt.subplot(1, 4, 4)
        plt.plot(hist_v, color='b')
        plt.title('Value Histogram')
        plt.xlim([0, 256])

        plt.suptitle(f'Image {i + 1} HSV Features')
        plt.show()

# Specify the directories containing the train and test images
train_directory = "D:\\new maize wheat\\train\\jpg"
test_directory = "D:\\new maize wheat\\test\\jpg"

# Load and convert images to HSV for both train and test directories
train_images = load_and_convert_images_to_hsv(train_directory)
test_images = load_and_convert_images_to_hsv(test_directory)

# Visualize HSV features for the first image from each set
if train_images:
    visualize_hsv_features([img[0] for img in train_images[:1]], [img[1] for img in train_images[:1]])
if test_images:
    visualize_hsv_features([img[0] for img in test_images[:1]], [img[1] for img in test_images[:1]])


# %%
import cv2
import os
import matplotlib.pyplot as plt

def load_images(directory):
    """Load images from a directory."""
    images = []
    for filename in os.listdir(directory):
        img_path = os.path.join(directory, filename)
        if os.path.isfile(img_path):
            img = cv2.imread(img_path)
            images.append(img)
    return images

def visualize_hsv_features(original_images):
    """Visualize the original image and the HSV histograms for the given images."""
    for i, original_img in enumerate(original_images):
        plt.figure(figsize=(15, 6))
        
        # Convert image to HSV
        hsv_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)

        # Plot original image
        plt.subplot(1, 4, 1)
        plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
        plt.title('Original Image')
        plt.axis('off')

        # Calculate histograms
        hist_h = cv2.calcHist([hsv_img], [0], None, [256], [0, 256])  # Hue
        hist_s = cv2.calcHist([hsv_img], [1], None, [256], [0, 256])  # Saturation
        hist_v = cv2.calcHist([hsv_img], [2], None, [256], [0, 256])  # Value
        
        # Plot histograms
        plt.subplot(1, 4, 2)
        plt.plot(hist_h, color='r')
        plt.title('Hue Histogram')
        plt.xlim([0, 256])

        plt.subplot(1, 4, 3)
        plt.plot(hist_s, color='g')
        plt.title('Saturation Histogram')
        plt.xlim([0, 256])

        plt.subplot(1, 4, 4)
        plt.plot(hist_v, color='b')
        plt.title('Value Histogram')
        plt.xlim([0, 256])

        plt.suptitle(f'Image {i + 1} HSV Features')
        plt.show()

# Specify the paths of the images directly
image_paths = [
    "D:\\new maize wheat\\train\\processed\\leaf_rust\\00VVPB.jfif",
    "D:\\new maize wheat\\train\\processed\\healthy_wheat\\03TD19.jfif"
]

# Load images from the specified paths
images = [cv2.imread(path) for path in image_paths if os.path.isfile(path)]

# Visualize HSV features for both images
visualize_hsv_features(images)


# %%



# %%
# Load the trained model and label encoder
model_file_path = 'random_forest_model.pkl'
loaded_model = joblib.load(model_file_path)
label_encoder = joblib.load('label_encoder.pkl')  # Ensure you have this file saved

print("Model and label encoder loaded successfully.")

# Function to predict a single image
def predict_single_image(image_path, model, label_encoder):
    image = cv2.imread(image_path)

    if image is not None:
        image = cv2.resize(image, (128, 128))
        feature = image.flatten().reshape(1, -1)
        prediction = model.predict(feature)
        predicted_label = label_encoder.inverse_transform(prediction)[0]

        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(f'Predicted: {predicted_label}')
        plt.axis('off')
        plt.show()

        return predicted_label
    else:
        print("Image not found or unable to load.")
        return None

# Path to the single image you want to predict
single_image_path = "D:\\maize,wheat\\train\\train\\stem_rust\\00LAS4.JPG"# Update with your actual image path
predicted_label = predict_single_image(single_image_path, loaded_model, label_encoder)

print(f"The predicted label for the image is: {predicted_label}")


# %%
import os
import matplotlib.pyplot as plt
from PIL import Image

# Set the path to your dataset directory
dataset_path = "D:\\new maize wheat\\train\\processed"

# List all folders in the dataset directory
folders = os.listdir(dataset_path)

# Number of images to display from each folder
num_images = 2

# Create a figure for plotting
plt.figure(figsize=(6, 6))

# Loop through each folder and display the first two images
for idx, folder in enumerate(folders):
    folder_path = os.path.join(dataset_path, folder)
    
    # Check if it's a directory
    if os.path.isdir(folder_path):
        # Get all images in the folder
        images = [img for img in os.listdir(folder_path) if img.endswith(('.png', '.jpg', '.jpeg'))]
        
        # Limit to first num_images or available images
        selected_images = images[:num_images]

        for i, image_name in enumerate(selected_images):
            img_path = os.path.join(folder_path, image_name)
            img = Image.open(img_path)

            # Create a subplot for each image
            plt.subplot(len(folders), num_images, idx * num_images + i + 1)
            plt.imshow(img)
            plt.axis('off')
            plt.title(folder)  # Set title as folder name

# Adjust layout
plt.tight_layout()
plt.show()


# %%
import os
import matplotlib.pyplot as plt
from PIL import Image

# Set the path to your dataset directory
dataset_path = "D:\\new maize wheat\\train\\processed"

# List all folders in the dataset directory
folders = os.listdir(dataset_path)

# Number of images to display from each folder
num_images = 2

# Create a smaller figure for plotting
plt.figure(figsize=(num_images * 2, len(folders) * 2))

# Loop through each folder and display the first two images
for idx, folder in enumerate(folders):
    folder_path = os.path.join(dataset_path, folder)
    
    # Check if it's a directory
    if os.path.isdir(folder_path):
        # Get all images in the folder
        images = [img for img in os.listdir(folder_path) if img.endswith(('.png', '.jpg', '.jpeg', '.jfif'))]
        
        # Limit to first num_images or available images
        selected_images = images[:num_images]

        for i, image_name in enumerate(selected_images):
            img_path = os.path.join(folder_path, image_name)
            img = Image.open(img_path)

            # Create a subplot for each image
            plt.subplot(len(folders), num_images, idx * num_images + i + 1)
            plt.imshow(img)
            plt.axis('off')
            plt.title(folder, fontsize=8)  # Smaller title font size

# Adjust layout and display the plot
plt.tight_layout()
plt.show()


# %%



