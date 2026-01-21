import sympy as sp
"""
Calculate the derivative of a cubic polynomial function.
This module demonstrates symbolic differentiation using SymPy.
It defines a function f(x) = (2x + 6)^3, computes its derivative,
and prints the simplified result.
Functions:
    None (script-based execution)
Variables:
    x (sp.Symbol): Symbolic variable representing the independent variable
    f (sp.Expr): The original function (2x + 6)^3
    f_prime (sp.Expr): The first derivative of f(x)
Example:
    Running this script will output the derivative of f(x) = (2x + 6)^3
    in simplified form.
"""
# Import the sympy library for symbolic mathematics
# Create a symbolic variable 'x' to use in mathematical expressions
# Define the function f(x) = (2x + 6)^3
# This is a cubic polynomial function composed of a linear expression
# Compute the first derivative of f with respect to x
# sp.diff() performs symbolic differentiation
# Print the derivative in simplified form
# sp.simplify() reduces the expression to its simplest form

# Definisikan variabel x
x = sp.Symbol('x')

# Tulis fungsi sesuai catatanmu
f = (2*x + 6)**3

# Perintahkan Python untuk mencari turunannya
f_prime = sp.diff(f, x)

print(f"Turunan dari f(x) adalah: {sp.simplify(f_prime)}")

