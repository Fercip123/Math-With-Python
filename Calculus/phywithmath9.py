import sympy as sp

t = sp.Symbol('t')
# Fungsi Kecepatan AI (Model kita)
v = 3*t**2 + 2*t

# 1. TURUNAN: Mencari tingkat perubahan (Optimizer)
# Memberitahu AI seberapa cepat ia harus berubah (Gradient)
akselerasi = sp.diff(v, t)
akselerasi = sp.diff(v, t)

# 2. INTEGRAL: Mencari akumulasi total (Metric)
# Memberitahu AI total jarak yang sudah ditempuh (Area under curve)
jarak_total = sp.integrate(v, (t, 0, 5)) # Jarak dari detik 0 ke 5

print(f"Laju Perubahan (Turunan): {akselerasi}")
print(f"Total Akumulasi dari t=0 ke t=5 (Integral): {jarak_total}")