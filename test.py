import skimage as ski
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib as mpl

### To test all thresholding filters

# img = Image.open("/home/dtzi/Desktop/petite/30-06-2025/Far11D0.Tif")
# pixels = np.array(img.getdata())
# pixels = pixels.reshape((2048,2048))
# fig, ax = ski.filters.try_all_threshold(pixels, figsize = (10,6), verbose = False)
# plt.show()

### To apply a single filter

img = Image.open("/home/dtzi/Desktop/petite/30-06-2025/Far12D0.Tif")
pixels = np.array(img.getdata())
pixels = pixels.reshape((2048,2048))
thresh = ski.filters.threshold_yen(pixels)
binary_img = pixels > thresh # manipulate threshold for different results, but best case scenario it doesnt get changed
binary_img2 = pixels < 60
fig, ax = plt.subplots(ncols = 3, figsize = (8,8))
ax[0].imshow(binary_img, cmap = mpl.colormaps["grey"]) # more on colormaps: https://matplotlib.org/stable/users/explain/colors/colormaps.html
ax[1].imshow(binary_img2, cmap = mpl.colormaps["grey"]) # more on colormaps: https://matplotlib.org/stable/users/explain/colors/colormaps.html
ax[2].imshow(img, cmap = mpl.colormaps["grey"])
plt.show()

