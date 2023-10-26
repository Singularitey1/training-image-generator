import os
import shutil

if os.path.exists("training-image-generator/background_images") and os.path.exists("training-image-generator/object_images"):
    num = 1
    while os.path.exists("training-image-generator/saved_input_images/saved_input_images_" + str(num)):
        num += 1

    shutil.copytree("training-image-generator/background_images", "training-image-generator/saved_input_images/saved_input_images_" + str(num) + "/saved_backgrounds")
    shutil.copytree("training-image-generator/object_images", "training-image-generator/saved_input_images/saved_input_images_" + str(num) + "/saved_objects")

print("Saved input images in saved_input_images/saved_input_images_" + str(num))