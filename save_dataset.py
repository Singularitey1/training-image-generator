import os
import shutil

if os.path.exists("training-image-generator/result_images"):
    num = 1
    while os.path.exists("training-image-generator/saved_datasets/saved_dataset_" + str(num)):
        num += 1

    shutil.copytree("training-image-generator/result_images", "training-image-generator/saved_datasets/saved_dataset_" + str(num))

print("Saved dataset in saved_datasets/saved_dataset_" + str(num))