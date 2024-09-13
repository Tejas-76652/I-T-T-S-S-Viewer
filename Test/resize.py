import os
from PIL import Image

def resize_image(input_folder='assets', output_folder='output', size=(256, 256)):
    # Get the list of images
    images = []
    for file in os.listdir(input_folder):
        if file.endswith(('.png', '.jpg', '.jpeg')):
            images.append(file)

    if not images:
        print(f"No images found in {input_folder}.")
        return

    # Display available images
    print("Available images:")
    for i, img in enumerate(images, 1):
        print(f"{i}. {img}")

    # Ask user to select an image by index
    choice = int(input(f"Select an image (1 to {len(images)}): ")) - 1
    if choice < 0 or choice >= len(images):
        print("Invalid choice.")
        return

    image_path = os.path.join(input_folder, images[choice])
    
    # Open and resize the selected image
    image = Image.open(image_path)
    resized_image = image.resize(size)

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create a unique filename by appending '_resized'
    base, ext = os.path.splitext(images[choice])
    new_filename = f"{base}_resized{ext}"

    # Save resized image
    resized_image.save(os.path.join(output_folder, new_filename))
    print(f"Resized {images[choice]} and saved as {new_filename} in {output_folder}.")

# Example usage
resize_image(size=(30, 30))
