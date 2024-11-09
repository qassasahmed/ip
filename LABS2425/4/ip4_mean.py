from skimage import data, io, filters
from skimage.morphology import square
import matplotlib.pyplot as plt

footprint = square(3)
image = io.imread('Noise_salt_and_pepper.png', as_gray=True)

smoothed_median = filters.median(image, footprint)
smoothed_mean = filters.rank.mean(image, footprint)
smoothed_gaussian = filters.gaussian(image, sigma=2) 

fig, ax = plt.subplots(1, 4)
ax[0].imshow(image, cmap='gray')
ax[1].imshow(smoothed_median, cmap='gray')
ax[2].imshow(smoothed_mean, cmap='gray')
ax[3].imshow(smoothed_gaussian, cmap='gray')

titles = ['Original', 'Median (3)', 'Mean (3)', 'Gaussian (Sigma=2)']
for i in range(len(ax)):
               ax[i].set_title(titles[i])
               ax[i].axis('off')
plt.show()

