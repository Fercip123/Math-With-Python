import math
"""
Approximate the exponential function e^x using Taylor series expansion.
The Taylor series expansion of e^x is:
e^x = 1 + x + x²/2! + x³/3! + ... + x^n/n!
Args:
    x (float): The exponent value for which to calculate e^x
    n_terms (int): The number of terms to include in the Taylor series approximation
Returns:
    float: The approximated value of e^x using the specified number of terms
Example:
    >>> taylor_exponential(0.2, 3)
    1.2214026666666667
    >>> taylor_exponential(0.2, 5)
    1.2214027447221765
Notes:
    - More terms generally lead to higher accuracy
    - The approximation converges to the true value of e^x as n_terms increases
    - Uses math.factorial() to compute factorial values
"""
prediction = 0  # Initialize accumulator for sum of terms
    # Calculate each term: x^i / i!
    # Add current term to the running sum

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

# Calculate the error/difference between Taylor approximation and actual value
error = abs(taylor_exponential(0.2, 3) - math.exp(0.2))
print(f"Error: {error}")

# Test with different number of terms to see accuracy improvement
print("\nAccuracy with different terms:")
for n in range(1, 6):
    approx = taylor_exponential(0.2, n)
    error = abs(approx - math.exp(0.2))
    print(f"Terms: {n}, Approximation: {approx:.10f}, Error: {error:.10e}")

