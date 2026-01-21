import numpy as np
"""
Gradient Descent Optimization Visualization
This module demonstrates the gradient descent algorithm, a fundamental optimization
technique used in machine learning to find the minimum of a cost function.
The script simulates a ball rolling down a hill to find the lowest point (minimum),
where:
- The hill represents the cost function: f(x) = x² - 4x + 3
- The ball's movement represents the iterative optimization process
- The learning rate controls how large each step should be
Key Components:
    - f(x): The cost function we want to minimize (quadratic function)
    - df(x): The derivative (gradient) that tells us the slope direction
    - learning_rate: Controls step size (how far the ball jumps each iteration)
    - steps: Number of iterations to run the algorithm
    - history_x: Tracks all positions visited during optimization
The algorithm works by:
    1. Starting at an initial position (x_start)
    2. Computing the gradient (slope) at current position
    3. Moving opposite to the gradient direction by (learning_rate * gradient)
    4. Repeating until convergence or max steps reached
Visualization shows:
    - Blue curve: The cost function landscape
    - Red dots and lines: The ball's path as it descends to the minimum
    - This illustrates how AI learns by iteratively improving its predictions
"""
import matplotlib.pyplot as plt

# 1. Definisi fungsi dan turunan dari catatanmu
def f(x): return x**2 - 4*x + 3
def df(x): return 2*x - 4

# 2. Parameter "Belajar" (Hyperparameters)
x_start = 0.5       # Posisi awal bola (mulai dari kanan)
learning_rate = 0.1 # Seberapa jauh bola melompat setiap langkah
steps = 20          # Berapa kali bola bergulir

# 3. Proses Algoritma Gradient Descent
history_x = [x_start]
current_x = x_start

for _ in range(steps):
    # Rumus utama: kurangi posisi sekarang dengan (turunan * kecepatan belajar)
    current_x = current_x - learning_rate * df(current_x)
    history_x.append(current_x)

# 4. Visualisasi
x_range = np.linspace(-1, 5, 100)
plt.figure(figsize=(10, 6))
plt.plot(x_range, f(x_range), label='Garis Bukit (Cost Function)', color='blue', alpha=0.6)

# Menggambar lompatan bola
history_x = np.array(history_x)
plt.plot(history_x, f(history_x), 'ro-', label='Gerakan Bola (AI Learning)')

plt.title("Simulasi Gradient Descent: Mencari Nilai Minimum")
plt.xlabel("X (Parameter)")
plt.ylabel("Y (Error/Cost)")
plt.legend()
plt.grid(True)
plt.show()
