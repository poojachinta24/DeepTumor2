import numpy as np
import cv2
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

def draw_red_box(image, x, y, width, height):
    # Define the box coordinates
    top_left = (x, y)
    bottom_right = (x + width, y + height)
    
    # Draw a red rectangle around the tumor
    color = (255, 0, 0)  # Red color in RGB
    thickness = 1  # Thickness of the rectangle border
    cv2.rectangle(image, top_left, bottom_right, color, thickness)
    
    # Display the image with the red box
    plt.imshow(image)
    plt.axis('off')  # Hide axis
    plt.show()

def make_further_processes(image):
    # Example pixel spacing in millimeters
    pixel_spacing = [0.5, 0.5]  # Example: 0.5 mm per pixel in both directions

    # Load and preprocess the MRI image
    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (64, 64))  # Resize image to (64, 64)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)  # Convert grayscale to RGB
    image = image / 255.0

    # Thresholding to segment the tumor
    _, thresh_image = cv2.threshold(image[:, :, 0], 0.5, 1, cv2.THRESH_BINARY)

    # Find contours to locate the tumor
    contours, _ = cv2.findContours(thresh_image.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        tumor_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(tumor_contour)
        
        # Determine the location
        height, width = image.shape[:2]
        center_x, center_y = x + w // 2, y + h // 2
        location = "Unknown"
        if center_x < width / 2 and center_y < height / 2:
            location = "Top Left"
        elif center_x > width / 2 and center_y < height / 2:
            location = "Top Right"
        elif center_x < width / 2 and center_y > height / 2:
            location = "Bottom Left"
        elif center_x > width / 2 and center_y > height / 2:
            location = "Bottom Right"
        else:
            location = "Center"

        # Calculate physical size (in millimeters)
        tumor_width_mm = w * pixel_spacing[0]
        tumor_height_mm = h * pixel_spacing[1]
        tumor_size_mm2 = tumor_width_mm * tumor_height_mm

        print(f"Tumor Location: {location}")
        print(f"Tumor Width: {tumor_width_mm:.2f} mm")
        print(f"Tumor Height: {tumor_height_mm:.2f} mm")
        print(f"Tumor Area: {tumor_size_mm2:.2f} mm²")

        post_process = {
            "location": location,
            "width": tumor_width_mm,
            "height": tumor_height_mm,
            "area": tumor_size_mm2
        }
        return post_process
