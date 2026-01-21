import numpy as np
"""
Module: Visualize Chain Rule with Tangent Line
This module demonstrates the chain rule in calculus by visualizing a composite function
and its tangent line at a specific point.
Functions:
    f(x): Computes the original function (2x + 6)^3
    df(x): Computes the derivative using the chain rule: 6 * (2x + 6)^2
    tangent_line(x): Computes the equation of the tangent line at point (x1, y1)
Main Process:
    1. Define the function f(x) = (2x + 6)^3 and its derivative df(x) using chain rule
    2. Generate x values in range [-5, -1] and compute corresponding y values
    3. Select a point x1 = -2.5 to analyze the rate of change
    4. Calculate the slope at x1 using the derivative (chain rule result: u' * n * u^(n-1))
    5. Create a tangent line equation using point-slope form: y = m(x - x1) + y1
    6. Plot the function curve, tangent line, and the point of tangency
    7. Display the visualization with labels and grid
Visualization Elements:
    - Blue curve: Original function (2x + 6)^3
    - Red dashed line: Tangent line at x1 = -2.5 showing instantaneous rate of change
    - Black dot: Point of tangency (x1, y1)
Purpose: Illustrates how the chain rule helps find the slope of composite functions
"""
import matplotlib.pyplot as plt

# Import libraries for numerical computing and visualization
# 1. Definisi fungsi asli dan hasil aturan rantaimu
def f(x): return (2*x + 6)**3
def df(x): return 6 * (2*x + 6)**2

# 2. Setup data grafik
x_vals = np.linspace(-5, -1, 100) # Kita ambil area sekitar titik belok
y_vals = f(x_vals)

# 3. Tentukan satu titik untuk melihat "Rantai" perubahannya
x1 = -2.5
y1 = f(x1)
kemiringan = df(x1) # Ini adalah hasil u' * n * u^(n-1)

# 4. Membuat garis singgung (Tangent Line)
# Rumus: y = m(x - x1) + y1
def tangent_line(x): return kemiringan * (x - x1) + y1
x_tangent = np.linspace(x1-0.5, x1+0.5, 10)

# 5. Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='Fungsi: $(2x + 6)^3$', color='blue', lw=2)
plt.plot(x_tangent, tangent_line(x_tangent), '--', label=f'Garis Singgung (m={kemiringan})', color='red')
plt.scatter([x1], [y1], color='black', zorder=5)

plt.title("Visualisasi Aturan Rantai: Perubahan Berantai")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

