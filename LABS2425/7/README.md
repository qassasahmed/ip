# Lab 7: Detecting Lines and Circles 
Dr. Amr Amin  
Ahmed Alqassas  
Autumn 2024-25    

## Hough Line Transform  
The **Hough Line Transform** is a technique to detect straight lines in an image. It maps edge points in Polar coordinates to a parameter space where potential lines can be identified.    

$\rho = x \cdot \cos(\theta) + y \cdot \sin(\theta)$

![Line Equation with Polar Coordinates](image-1.png)

Where:
- $\rho$: Perpendicular distance from the origin to the line.
- $\theta$: Angle between the perpendicular line and the horizontal axis.

In the Hough Transform:
1. Each edge point $(x, y)$ in the image contributes a sinusoidal curve in the $(\rho, \theta)$ parameter space.
2. Intersections of these curves correspond to potential lines.

### Algorithm
1. **Edge Detection**: Use a technique like **Canny** to detect edges in the image.
2. **Parameter Space Accumulation**:
   - For each edge point $(x, y)$:
     - Compute $\rho$ for a range of  $\theta$ values.
     - Increment the accumulator at $\rho$, $\theta$.
3. **Thresholding**:
   - Identify peaks in the accumulator space that exceed a certain threshold.
4. **Line Reconstruction**:
   - Convert the detected $(\rho, \theta)$ back into line endpoints in Cartesian coordinates for visualization.

### Function
```Python
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
```
### Parameters
1. **`edges`**:  
   - **Type**: Input image (binary).  
   - **Description**: The binary image resulting from edge detection (e.g., Canny).  
   - Edge pixels are white (non-zero), and the background is black (zero).

2. **`1` (rho resolution)**:  
   - **Type**: `float`.  
   - **Description**: The resolution of the accumulator in terms of the distance parameter $\rho$ (in pixels).  
   - A value of `1` means the distance resolution is 1 pixel.  

   > **Why rho resolution?** Since $\rho$ can take any real value, it must be **quantized** into discrete bins in the accumulator array for practical computation. Hence, The $\rho$-resolution directly affects the precision of the accumulator:

 Distance Resolution $\rho$ | Pros                                         | Cons                                |
|----------------------------------|---------------------------------------------|-------------------------------------|
| \( 1 \) pixel                    | Faster computation, sufficient for most cases | Coarser distance detection, may merge nearby lines |
| \( 0.5 \) pixels                 | Finer detection of closely spaced lines      | Slower computation, may detect more noise   |  


3. **`np.pi / 180` (theta resolution)**:  
   - **Type**: `float`.  
   - **Description**: The resolution of the accumulator in terms of the angle parameter $\theta$ (in radians).  
   - A value of `np.pi / 180` corresponds to 1 degree: $radians = degrees \times \frac{\pi}{180}$  

| Angular Resolution $\theta$| Pros                                         | Cons                                |
|---------------------|---------------------------------------------|-------------------------------------|
| $1^\circ$       | Faster computation, sufficient for most use cases | Coarser detection, might miss subtle angles |
| $0.5^\circ$  | Finer detection, higher precision           | Slower computation, may detect more noise   |  

4. **`200` (threshold)**:  
   - **Type**: `int`.  
   - **Description**: The threshold for the accumulator.  
     - Only those $(\rho, \theta)$ values that have at least `200` votes in the accumulator are considered as detected lines.  
     - Increasing this value reduces the number of detected lines (useful for noisy images).  

> higher threshold decreases the numeber of detected lines.  

### Output
**`lines`**:  
  - **Type**: array of shape `(N, 1, 2)`, where `N` is the number of detected lines.  
  - **Description**: Each detected line is represented by the pair $(\rho, \theta)$:  
    - $\rho$: The perpendicular distance from the origin to the line.  
    - $\theta$: The angle of the line with respect to the x-axis, in radians
---

## Hough Circle Transform
- The Hough Circle Transform identifies circular shapes in an image using edge detection and parameter space voting.
- Detected circles are returned as $(x, y, r)$, representing the center coordinates and radius.  

### Algorithm
1. **Edge Detection**:  
   - Uses the Canny edge detector to find edges in the input image.

2. **Parameter Space Accumulation**:  
   - For each edge point $(x, y)$, calculate all possible circles that could pass through the point for various radii.  
   - Accumulate votes for each $(x, y, r)$ triplet in the parameter space.

3. **Thresholding**:  
   - Only retain $(x, y, r)$ triplets where the number of votes exceeds the `param2` threshold.

4. **Circle Reconstruction**:  
   - The function returns the $(x, y, r)$ triplets representing the detected circles.

### Function
```python
circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=10, maxRadius=50)
```

This line detects circles in an input image using the Hough Circle Transform.  
### Parameters

1. **`image`**:  
   - **Type**: Input image (grayscale).  
   - **Description**: The source image where circles are to be detected. It must be a single-channel, 8-bit image (e.g., grayscale).

2. **`cv2.HOUGH_GRADIENT`**:  
   - **Type**: Detection method.  
   - **Description**: Specifies the method used for detection. The only currently implemented method is `cv2.HOUGH_GRADIENT`, which uses edge detection and a circular accumulator.

3. **`1` (dp)**:  
   - **Type**: `float`.  
   - **Description**: The inverse ratio of the accumulator resolution to the image resolution.  
     - A value of `1` means the accumulator has the same resolution as the input image.  
     - A value of `2` means the accumulator resolution is half the image resolution.

4. **`20` (minDist)**:  
   - **Type**: `float`.  
   - **Description**: Minimum distance between the centers of detected circles.  
     - Reduces the likelihood of detecting multiple circles around the same location.

5. **`param1`**:  
   - **Type**: `float`.  
   - **Description**: The higher threshold for the Canny edge detector. The lower threshold is half of this value.

6. **`param2`**:  
   - **Type**: `float`.  
   - **Description**: The accumulator threshold for circle detection.  
     - Only those circles whose votes exceed this threshold will be returned.

7. **`minRadius`**:  
   - **Type**: `int`.  
   - **Description**: Minimum circle radius to be detected.  
     - Helps avoid detecting very small or irrelevant circles.

8. **`maxRadius`**:  
   - **Type**: `int`.  
   - **Description**: Maximum circle radius to be detected.  
     - Helps avoid detecting excessively large circles.

### Output
- **`circles`**:  
   - **Type**: array of shape `(1, N, 3)` or `None`, where `N` is the number of detected circles.  
   - **Description**: Each detected circle is represented by the tuple `(x, y, r)`:
     - `x`: X-coordinate of the circle's center.
     - `y`: Y-coordinate of the circle's center.
     - `r`: Radius of the circle.

---
## References
1. https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
2. https://docs.opencv.org/3.4/da/d53/tutorial_py_houghcircles.html
3. https://docs.opencv.org/3.4/da/d5c/tutorial_canny_detector.html
