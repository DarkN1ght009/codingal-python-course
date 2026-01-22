import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image."""
    # Create a copy of the image to avoid modifying the original
    filtered_image = image.copy()

    # Note: OpenCV uses BGR format (0: Blue, 1: Green, 2: Red)
    if filter_type == "red_tint":
        # Remove blue and green channels for red tint
        filtered_image[:, :, 0] = 0  # Blue channel to 0
        filtered_image[:, :, 1] = 0  # Green channel to 0
        
    elif filter_type == "blue_tint":
        # Remove red and green channels for blue tint
        filtered_image[:, :, 1] = 0  # Green channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0
        
    elif filter_type == "green_tint":
        # Remove blue and red channels for green tint
        filtered_image[:, :, 0] = 0  # Blue channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0
        
    elif filter_type == "increase_red":
        # Increase the intensity of the red channel
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
        
    elif filter_type == "decrease_blue":
        # Decrease the intensity of the blue channel
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
        
    return filtered_image

# Load the image
image_path = 'example.jpg'  # Provide your image path
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red")
    print("d - Decrease Blue")
    print("o - Original")
    print("q - Quit")

    current_filter = "original"

    while True:
        # Get the filtered version
        result = apply_color_filter(image, current_filter)
        
        # Display the result
        cv2.imshow('Image Filter', result)
        
        # Capture keystroke
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('r'):
            current_filter = "red_tint"
        elif key == ord('b'):
            current_filter = "blue_tint"
        elif key == ord('g'):
            current_filter = "green_tint"
        elif key == ord('i'):
            current_filter = "increase_red"
        elif key == ord('d'):
            current_filter = "decrease_blue"
        elif key == ord('o'):
            current_filter = "original"
        elif key == ord('q'):
            break

        else:
            print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', or 'q'.")

cv2.destroyAllWindows()