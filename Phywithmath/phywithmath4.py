import numpy as np

# Fungsi yang meledak (seperti bunga majemuk atau pertumbuhan populasi tak terkendali)
def f_meledak(x):
    """
    Calculates the exponential function e^x (exponential growth).
    This function demonstrates explosive/unbounded growth behavior, similar to:
    - Compound interest calculations
    - Uncontrolled population growth
    - Radioactive decay (inverse)
    Args:
        x (float or int): The exponent value
    Returns:
        float: The result of e raised to the power of x (e^x)
    Examples:
        >>> f_meledak(1)
        2.718281828459045
        >>> f_meledak(10)
        22026.465794806713
    Note:
        The function exhibits explosive growth - small increases in x result in 
        dramatically larger output values. For example:
        - x=1 gives ~2.72
        - x=10 gives ~22,026
        - x=100 gives ~2.69e+43
        - x=1000 gives infinity (overflow in standard floating-point)
    """
    return np.exp(x) # e pangkat x

# Mari kita lihat apa yang terjadi jika x semakin besar
for x in [1, 10, 100, 1000]:
    hasil = f_meledak(x)
    print(f"Jika x = {x}, maka hasil = {hasil}")

