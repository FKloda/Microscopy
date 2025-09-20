from cellpose import models, io
import numpy as np
import glob
import os
import skimage.morphology
import matplotlib.pyplot as plt

# Load pretrained model for nuclei
model = models.CellposeModel(pretrained_model='cpsam')

input_dir = "C:/Skola/Microscopy/validation/images/"
output_dir = "C:/Skola/Microscopy/validation/predictions/"
os.makedirs(output_dir, exist_ok=True)

# for img_path in glob.glob(os.path.join(input_dir, "*.tif")):
#     img = io.imread(img_path)
#     masks, flows, styles, diams = model.eval(img, diameter=None, channels=[0,0])
#     out_path = os.path.join(output_dir, os.path.basename(img_path))
#     io.imsave(out_path, masks.astype(np.uint16))

img_path = "C:\\Skola\\Microscopy\\validation\\images\\IXMtest_A02_s1_w1051DAA7C-7042-435F-99F0-1E847D9B42CB.tif"
img = io.imread(img_path)
masks, flows, styles = model.eval(img, diameter=None, channels=[0,0])
out_path = os.path.join(output_dir, os.path.basename(img_path))
io.imsave(out_path, masks.astype(np.uint16))

gt = skimage.morphology.label(masks)

plt.imshow(gt)

plt.show()
