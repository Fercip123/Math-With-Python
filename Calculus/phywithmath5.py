import sympy as sp

# Definisikan variabel x
x = sp.Symbol('x')

# Tulis fungsi sesuai catatanmu
f = (2*x + 6)**3

# Perintahkan Python untuk mencari turunannya
f_prime = sp.diff(f, x)

print(f"Turunan dari f(x) adalah: {sp.simplify(f_prime)}")