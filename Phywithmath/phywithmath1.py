import matplotlib.pyplot as plt
"""
Visualization of Derivative as the Slope of a Tangent Line
This module demonstrates the geometric interpretation of derivatives by plotting
a function and its tangent line at a specific point.
Functions:
    f(x): Computes the original function value 2x^2 - 4x
    df(x): Computes the derivative (slope) at point x, which is 4x - 4
The script performs the following operations:
    1. Defines the original function f(x) = 2x^2 - 4x and its derivative df(x) = 4x - 4
    2. Generates x-range data points from -1 to 5 for plotting the function curve
    3. Calculates the tangent line at x = 3:
       - Finds the y-coordinate on the curve: y1 = f(3) = 6
       - Calculates the slope (derivative) at that point: m = df(3) = 8
       - Uses point-slope form to generate tangent line coordinates
    4. Creates a visualization showing:
       - The original parabolic curve in blue
       - The tangent line at x=3 in red dashed line
       - The point of tangency marked with a red dot
       - Coordinate axes and grid for reference
This demonstrates that the derivative at a point represents the slope of the
tangent line to the function at that point.
Author: Physics with Math Student
Output: Matplotlib figure showing the function and tangent line
"""
import numpy as np

# 1. Definisi fungsi asli dan turunannya dari catatanmu
def f(x): return 2*x**2 - 4*x
def df(x): return 4*x - 4  # Hasil perhitunganmu: 4x - 4

# 2. Setup data grafik
x_range = np.linspace(-1, 5, 100)
y_range = f(x_range)

# 3. Hitung garis singgung di titik x = 3
x1 = 3
y1 = f(x1)      # Titik y di kurva
m = df(x1)      # Kemiringan di titik tersebut (Turunan)
# Rumus garis: y - y1 = m(x - x1) -> y = m*(x - x1) + y1
tan_x = np.linspace(2, 4, 10)
tan_y = m * (tan_x - x1) + y1

# 4. Plotting
plt.figure(figsize=(8,6))
plt.plot(x_range, y_range, label='Fungsi Asli: $2x^2 - 4x$', color='blue')
plt.plot(tan_x, tan_y, label=f'Garis Singgung di x={x1} (m={m})', color='red', linestyle='--')
plt.scatter([x1], [y1], color='red') # Titik singgung

plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.title("Visualisasi Turunan sebagai Kemiringan Garis Singgung")
plt.legend()
plt.grid(True)
plt.show()

