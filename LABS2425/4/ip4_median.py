from skimage import data, io
from skimage import filters

import matplotlib.pyplot as plt

image = io.imread('Noise_salt_and_pepper.png', as_gray=True)
smoothed_image = filters.median(image)

titles = ['Original Image', 'Median Filtered Image']

fig, ax = plt.subplots(1, 2)

ax[0].imshow(image, cmap='gray')
ax[1].imshow(smoothed_image, cmap='gray')
for i in range(len(ax)):
    ax[i].axis('off')
    ax[i].set_title(titles[i])

plt.show()

