import math

def taylor_exponential(x, n_terms):
    prediction = 0
    for i in range(n_terms):
        # Rumus: x pangkat i dibagi i faktorial
        term = (x**i) / math.factorial(i)
        prediction += term
    return prediction

# Mari kita coba tebak e^0.2 dengan 3 suku (seperti latihan kita tadi)
print(f"Hasil Taylor (3 suku): {taylor_exponential(0.2, 3)}")
print(f"Hasil Asli (math.exp): {math.exp(0.2)}")