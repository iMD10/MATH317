def complete_horner_algorithm_with_remainders(coefficients, r):
    
    n = len(coefficients)
    deflated_coefficients = []  # To store coefficients of each deflated polynomial
    remainders = []  # To store the remainder p(r) at each step

    for k in range(n - 1):  # Iterate for n-1 steps of deflation
        # Store the leading coefficient (constant term for the remainder)
        remainders.append(coefficients[k])

        for j in range(n - 1, k, -1):  # Update coefficients a_j <- a_j + r * a_(j+1)
            coefficients[j - 1] += r * coefficients[j]

        # Save the current state of coefficients after each iteration
        deflated_coefficients.append(coefficients[:n - k - 1])

    # The last remaining coefficient is the final remainder
    remainders.append(coefficients[-1])

    return deflated_coefficients, remainders

# Example usage:
coefficients = [1, -6, 11, -6]  # For p(x) = x^3 - 6x^2 + 11x - 6
r = 2  # Root value to use for deflation
deflated_coeffs, remainders = complete_horner_algorithm_with_remainders(coefficients, r)

print("Deflated coefficients at each step:")
for step, coeffs in enumerate(deflated_coeffs, 1):
    print(f"Step {step}: {coeffs}")

print("\nRemainders at each step:")
for step, remainder in enumerate(remainders, 1):
    print(f"Step {step}: {remainder}")
