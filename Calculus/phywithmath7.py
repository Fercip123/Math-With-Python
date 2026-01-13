import numpy as np
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