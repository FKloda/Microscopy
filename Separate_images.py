import os
import io

# for filename in io.open('C:/Skola/Microscopy/metadata/metadata/validation.txt', 'r', encoding='utf-8'):
#     filename_tif = filename.split('.')[0] + '.tif'
#     os.replace("C:/Skola/Microscopy/images/images/" + filename_tif, "C:/Skola/Microscopy/validation/images/" + filename_tif)
#     os.replace("C:/Skola/Microscopy/masks/decoded/" + filename.strip(), "C:/Skola/Microscopy/validation/masks/" + filename.strip())

for filename in io.open('C:/Skola/Microscopy/metadata/metadata/training.txt', 'r', encoding='utf-8'):
    filename_tif = filename.split('.')[0] + '.tif'
    os.replace("C:/Skola/Microscopy/images/images/" + filename_tif, "C:/Skola/Microscopy/training/images/" + filename_tif)
    os.replace("C:/Skola/Microscopy/masks/decoded/" + filename.strip(), "C:/Skola/Microscopy/training/masks/" + filename.strip())

for filename in io.open('C:/Skola/Microscopy/metadata/metadata/test.txt', 'r', encoding='utf-8'):
    filename_tif = filename.split('.')[0] + '.tif'
    os.replace("C:/Skola/Microscopy/images/images/" + filename_tif, "C:/Skola/Microscopy/testing/images/" + filename_tif)
    os.replace("C:/Skola/Microscopy/masks/decoded/" + filename.strip(), "C:/Skola/Microscopy/testing/masks/" + filename.strip())
