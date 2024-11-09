import matplotlib.pyplot as plt
from skimage import data, filters
from skimage.color import rgb2gray

# Load and convert the sample image to grayscale
image = data.text()

# Apply sharpening filters
unsharp_image = filters.unsharp_mask(image, radius=2, amount=1.5)
laplacian_edges = filters.laplace(image)
blurred_image = filters.gaussian(image, sigma=2)
high_pass_image = image - blurred_image

# Display the original and filtered images
fig, axes = plt.subplots(1, 4, figsize=(20, 5), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(image, cmap='gray')
ax[0].set_title("Original Image")

ax[1].imshow(unsharp_image, cmap='gray')
ax[1].set_title("Unsharp Mask")

ax[2].imshow(laplacian_edges, cmap='gray')
ax[2].set_title("Laplacian Filter")

ax[3].imshow(high_pass_image, cmap='gray')
ax[3].set_title("High-Pass Filter")

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()
