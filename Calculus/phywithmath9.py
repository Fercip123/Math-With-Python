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

# Evaluate the expressions at a specific time point (t=2)
akselerasi_at_2 = akselerasi.subs(t, 2)
v_at_2 = v.subs(t, 2)

print(f"Kecepatan pada t=2: {v_at_2}")
print(f"Akselerasi pada t=2: {akselerasi_at_2}")
# Additional comments explaining the code

# The velocity function v = 3t² + 2t represents how fast the AI model changes over time
# Higher t values mean faster velocity

# Derivatives (turunan) show the rate of change - used in optimization to adjust model parameters
# akselerasi = 6t + 2 is the derivative, showing how quickly velocity changes

# Integration (integral) accumulates the total distance traveled from t=0 to t=5
# This represents the cumulative effect of the velocity over the time interval

# Substituting t=2 into the expressions gives us specific values at that moment in time
# This is useful for understanding model behavior at specific points during training
