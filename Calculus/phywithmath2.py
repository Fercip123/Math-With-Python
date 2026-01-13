import numpy as np
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