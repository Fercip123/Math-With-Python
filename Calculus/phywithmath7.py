import numpy as np
"""
Module: Visualization of Definite Integral Calculation
This module visualizes the definite integral of a quadratic function f(x) = 2x^2 - 2
over the interval [a=-1, b=2]. It plots the function curve and shades the area under
the curve to represent the calculated integral value.
Functions:
    f(x): Quadratic function defined as 2x^2 - 2
Usage:
    Run this script to display a matplotlib figure showing:
    - The parabola curve of f(x) = 2x^2 - 2
    - The shaded region representing the definite integral from x=-1 to x=2
    - The calculated area value (result = 1.5)
Dependencies:
    - numpy: For numerical array operations and linspace function
    - matplotlib.pyplot: For creating and displaying plots
Author: [Your Name]
Date: [Date]
Version: 1.0
"""
# Import required libraries for numerical computing and visualization
# Define the quadratic function f(x) = 2x^2 - 2
# Create array of x values across range [-2, 3] for smooth curve plotting (400 points)
# Create array of x values within integration bounds [-1, 2] for shading (100 points)
x_fill = np.linspace(-1, 2, 100)
# Calculate y values at integration bounds
# Initialize figure with specified dimensions
# Plot the function curve with label and formatting
# Draw the x-axis reference line
plt.axhline(0, color='black', lw=1)
# Shade the area under the curve between x=-1 and x=2 (definite integral region)
# Add title and axis labels
# Display legend and grid
# Render the plot
import matplotlib.pyplot as plt

# 1. Definisi fungsi dari catatanmu
def f(x): return 2*x**2 - 2

# 2. Rentang x untuk grafik dan area integral
x = np.linspace(-2, 3, 400)
x_fill = np.linspace(-1, 2, 100) # Batas integral a=-1, b=2
y_fill = f(x_fill)

# 3. Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, f(x), label='$f(x) = 2x^2 - 2$', color='blue', lw=2)
plt.axhline(0, color='black', lw=1) # Garis sumbu x

# Mengarsir daerah integral (Luas yang kamu hitung)
plt.fill_between(x_fill, y_fill, color='orange', alpha=0.4, 
                 label='Luas Daerah = 1.5 (Hasil Hitunganmu)')

plt.title("Visualisasi Hasil Integral Tentumu")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

