def deflate_polynomial(coefficients, r):
    
    n = len(coefficients)
    q_coefficients = [0] * (n - 1)  # To store coefficients of q(x)
    b = coefficients[-1]  # Start with the coefficient of the highest power term

    for i in range(n - 2, -1, -1):
        q_coefficients[i] = b
        b = coefficients[i] + r * b

    # p(r) is the final remainder (b from the last iteration)
    p_r = b
    return q_coefficients, p_r

# Example usage:
coefficients = [1, -6, 11, -6]  # p(x) = x^3 - 6x^2 + 11x - 6
r = 2  # Deflate by (x - 2)
q_coefficients, p_r = deflate_polynomial(coefficients, r)
print(f"Deflated polynomial coefficients (q(x)): {q_coefficients}")
print(f"Remainder (p(r)): {p_r}")
