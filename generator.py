import cv2
import os
import random

num_of_results = 50

# List background and object image folders
background_images = os.listdir("training-image-generator/background_images")
object_images = os.listdir("training-image-generator/object_images")

for i in range(num_of_results):
    try:
        # Randomly select a background image
        background = cv2.imread("training-image-generator/background_images/" + random.choice(background_images))

        # Loop through all object images and overlay each onto the background
        for obj_image_file in object_images:
            overlay = cv2.imread("training-image-generator/object_images/" + obj_image_file, cv2.IMREAD_UNCHANGED)

            # Calculate the height and width of the images
            bg_height, bg_width, _ = background.shape
            overlay_height, overlay_width, _ = overlay.shape

            # Calculate valid random positions to overlay the images
            y1 = random.randint(0, bg_height - overlay_height)
            x1 = random.randint(0, bg_width - overlay_width)
            y2 = y1 + overlay_height
            x2 = x1 + overlay_width

            # Crop the overlay image to fit within the bounds of the background
            overlay_cropped = overlay[0:overlay_height, 0:overlay_width]

            # Get the alpha channel from the overlay
            overlay_alpha = overlay_cropped[:, :, 3] / 255.0

            # Calculate the region of interest (ROI) on the background where the overlay will be placed
            bg_roi = background[y1:y2, x1:x2]

            # Blend the overlay onto the background using alpha blending
            for c in range(0, 3):
                bg_roi[:, :, c] = bg_roi[:, :, c] * (1 - overlay_alpha) + overlay_cropped[:, :, c] * overlay_alpha

            # Update the background with the blended ROI
            background[y1:y2, x1:x2] = bg_roi

            # Save the resulting image
            cv2.imwrite("training-image-generator/result_images/trainingImage" + str(i+1) + ".png", background)

        print("Training Image", i+1, "Done")
    except:
        print("Check to make sure BackgroundImages and ObjectImages contain images.")