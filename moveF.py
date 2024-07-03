import numpy as np
import os
import cv2 as cv

folder_path = "Faces"

image_files = os.listdir(folder_path)
image_files.sort()
for file_name in image_files:
    if file_name.endswith(".jpg"):
        folderName = file_name.split('_')[0]
        new_folder_path = os.path.join(folder_path, folderName)
        os.makedirs(new_folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(new_folder_path, file_name)
        os.rename(file_path, new_file_path)
