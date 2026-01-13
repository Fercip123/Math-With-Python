import matplotlib.pyplot as plt
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