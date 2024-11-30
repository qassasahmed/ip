# Bonus: Understanding the Canny Edge Detector Algorithm

The **Canny Edge Detector** is a multi-step algorithm used to detect edges in images. It was developed by John Canny in 1986 and is widely regarded as one of the most effective edge detection techniques.

---

## Steps of the Canny Edge Detector Algorithm

### 1. **Noise Reduction**
Images often contain noise that can interfere with edge detection. To reduce noise, the image is convolved with a **Gaussian filter**:

$G(x, y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}}$

Here:
- $\sigma$: Standard deviation of the Gaussian filter.
- $( x, y)$ Pixel coordinates.

This step smooths the image, reducing noise while preserving edges.

---

### 2. **Gradient Calculation**
The algorithm computes the intensity gradient of the image to detect edges. The gradient measures the change in intensity (\(I\)) along the \(x\)- and \(y\)-directions:

$
G_x = \frac{\partial I}{\partial x}, \quad G_y = \frac{\partial I}{\partial y}
$

The magnitude $(G)$ and direction $(\theta)$ of the gradient are calculated as:

$
G = \sqrt{G_x^2 + G_y^2}
$

$
\theta = \arctan\left(\frac{G_y}{G_x}\right)
$

> The magnitude indicates the strength of the edge, and the direction indicates its orientation.

---

### 3. **Non-Maximum Suppression**
To achieve thin edges, the algorithm suppresses non-maximum gradient magnitudes. For a pixel at $(x, y)$:
- Check the two neighboring pixels along the gradient direction $(\theta)$.
- If the pixel's gradient magnitude $G(x, y)$ is not the largest compared to its neighbors, set it to zero.

>This step ensures that only the strongest edge points are retained.

---

### 4. **Double Thresholding**
The algorithm applies two thresholds: a **low threshold** $T_{low}$ and a  **high threshold** $T_{high}$. Pixels are classified as:
- **Strong edges**: $G(x, y) > T_{high}$
- **Weak edges**: $T_{low} < G(x, y) \leq T_{high}$
- **Non-edges**: $G(x, y) \leq T_{low}$

---

### 5. **Edge Tracking by Hysteresis**
Weak edges are preserved only if they are connected to strong edges. This step eliminates spurious weak edges while maintaining continuous edge structures.

## Visualization of the Steps

1. **Original Image**: Input image.
2. **Smoothed Image**: Gaussian smoothing removes noise.
3. **Gradient Magnitude and Direction**: Highlights edge strength and orientation.
4. **Thin Edges**: Non-maximum suppression produces thin edges.
5. **Final Edges**: Double thresholding and hysteresis finalize edge detection.

---

## Applications of Canny Edge Detection
- Image segmentation
- Feature detection in computer vision
- Object recognition
