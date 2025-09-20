# Example instructions to decode ground truth masks in BBBC039
# Masks available at: https://data.broadinstitute.org/bbbc/BBBC039/masks.zip

import skimage.io
import matplotlib.pyplot as plt
import skimage.morphology
import os

files = os.listdir("C:/Skola/Microscopy/masks/masks")

for file in files:
# Load one image after uncompressing masks.zip
    path = "C:/Skola/Microscopy/masks/masks/" + file
    gt = skimage.io.imread(path)

    # Keep first channel only
    gt = gt[:,:,0]
    print(gt)
    # Label independent connected components
    gt = skimage.morphology.label(gt)

    outpath = "C:/Skola/Microscopy/masks/decoded/" + file
    # skimage.io.imsave(outpath, gt.astype('uint16'))
# Display image or use as needed
# plt.imshow(gt)
#
# plt.show()