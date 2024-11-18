def evaluate_polynomial(coefficients, x):
   
    p = coefficients[-1]  # Start with the coefficient of the highest degree term
    for i in range(len(coefficients) - 2, -1, -1):
        p = coefficients[i] + x * p
    return p

# Example usage:
coefficients = [1, -3, 2]  # For p(x) = 1 - 3x + 2x^2
x = 5
result = evaluate_polynomial(coefficients, x)
print(f"The polynomial evaluated at x = {x} is {result}")
