# Lab 7: Hough Line and Circle Transform  
Dr. Amr Amin  
Ahmed Alqassas  
Autumn 2024-25  
---
## Hough Line Transform  
The **Hough Line Transform** is a technique to detect straight lines in an image. It maps edge points in Polar coordinates to a parameter space where potential lines can be identified.

$\rho = x \cdot \cos(\theta) + y \cdot \sin(\theta)$

Where:
- \( \rho \): Perpendicular distance from the origin to the line.
- \( \theta \): Angle between the perpendicular line and the horizontal axis.

In the Hough Transform:
1. Each edge point \((x, y)\) in the image contributes a sinusoidal curve in the \((\rho, \theta)\) parameter space.
2. Intersections of these curves correspond to potential lines.
---

## Algorithm
1. **Edge Detection**: Use a technique like **Canny** to detect edges in the image.
2. **Parameter Space Accumulation**:
   - For each edge point \((x, y)\):
     - Compute \( \rho \) for a range of \( \theta \) values.
     - Increment the accumulator at \((\rho, \theta)\).
3. **Thresholding**:
   - Identify peaks in the accumulator space that exceed a certain threshold.
4. **Line Reconstruction**:
   - Convert the detected \((\rho, \theta)\) back into line endpoints in Cartesian coordinates for visualization.

---

