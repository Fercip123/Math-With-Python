import numpy as np
"""
Module: Definite Integral Visualization and Symbolic Verification
Description:
    This module demonstrates the calculation and visualization of a definite integral
    using both symbolic computation and numerical methods. It computes the definite
    integral of f(x) = (2x+1)^3 from 0 to 1 and creates a visual representation
    of the integrated area under the curve.
Main Components:
    1. Symbolic Integration: Uses SymPy to compute the exact definite integral
       from 0 to 1 of the function (2x+1)^3
    2. Visualization: Creates a matplotlib plot showing:
       - The curve of the function f(x) = (2x+1)^3
       - The shaded area under the curve between x=0 and x=1 (the integral region)
       - Grid, axes, labels, and legend for clarity
Dependencies:
    - numpy: For numerical operations and linspace array generation
    - matplotlib.pyplot: For plotting and visualization
    - sympy: For symbolic mathematics and exact integral calculation
Output:
    - Console output: The exact value of the definite integral
    - Visual output: A plot displaying the function curve and the integrated area
Usage:
    Run the script to compute the definite integral symbolically and display
    a visual representation of the area under the curve in the integration interval [0, 1].
"""
import matplotlib.pyplot as plt
import sympy as sp

# 1. Verifikasi Simbolik (Hitungan Pasti)
x_sym = sp.Symbol('x')
f_sym = (2*x_sym + 1)**3
hasil_pastis = sp.integrate(f_sym, (x_sym, 0, 1))

print(f"Hasil Integral Tentu (0 ke 1) menurut Python: {hasil_pastis}")

# 2. Visualisasi Grafik
def f(x): return (2*x + 1)**3

x_vals = np.linspace(-0.2, 1.2, 400)
y_vals = f(x_vals)

# Area integral (0 sampai 1)
x_fill = np.linspace(0, 1, 100)
y_fill = f(x_fill)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='$f(x) = (2x+1)^3$', color='blue', lw=2)
plt.fill_between(x_fill, y_fill, color='green', alpha=0.3, label=f'Luas (Integral) = {hasil_pastis}')

plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.title("Visualisasi Integral Tentu Latihan 3")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

