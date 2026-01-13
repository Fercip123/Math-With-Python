import numpy as np
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