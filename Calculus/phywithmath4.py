import numpy as np

# Fungsi yang meledak (seperti bunga majemuk atau pertumbuhan populasi tak terkendali)
def f_meledak(x):
    return np.exp(x) # e pangkat x

# Mari kita lihat apa yang terjadi jika x semakin besar
for x in [1, 10, 100, 1000]:
    hasil = f_meledak(x)
    print(f"Jika x = {x}, maka hasil = {hasil}")