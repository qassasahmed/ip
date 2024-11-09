import matplotlib.pyplot as plt
from skimage import data, filters, feature
from skimage.color import rgb2gray

image = rgb2gray(data.coffee())

sobel_edges = filters.sobel(image)
scharr_edges = filters.scharr(image)
prewitt_edges = filters.prewitt(image)
roberts_edges = filters.roberts(image)
canny_edges = feature.canny(image, sigma=1)

fig, axes = plt.subplots(2, 3, figsize=(15, 10), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(image, cmap='gray')
ax[0].set_title("Original Image")

ax[1].imshow(sobel_edges, cmap='gray')
ax[1].set_title("Sobel Filter")

ax[2].imshow(scharr_edges, cmap='gray')
ax[2].set_title("Scharr Filter")

ax[3].imshow(prewitt_edges, cmap='gray')
ax[3].set_title("Prewitt Filter")

ax[4].imshow(roberts_edges, cmap='gray')
ax[4].set_title("Roberts Filter")

ax[5].imshow(canny_edges, cmap='gray')
ax[5].set_title("Canny Edge Detection")

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()
