import numpy as np
import matplotlib.pyplot as plt

# Fungsi berliku dan turunannya
def f(x): return x**4 - 4*x**2 + x
def df(x): return 4*x**3 - 8*x + 1

x_range = np.linspace(-2.5, 2.5, 100)
# Simulasi: Mulai dari x = 0 (tengah bukit)
x_now = 0
lr = 0.05
history = [x_now]

for _ in range(20):
    x_now = x_now - lr * df(x_now)
    history.append(x_now)

plt.plot(x_range, f(x_range), label='Garis Bukit Kompleks')
plt.plot(history, f(np.array(history)), 'ro-', label='AI Terjebak?')
plt.title("Masalah Local Minima dalam NeuroAI")
plt.legend()
plt.show()