def compute_array(n, r, a):
    # Ensure the array has n+1 elements
    if len(a) != n + 1:
        raise ValueError("Array 'a' must have n+1 elements.")

    for k in range(n):
        for j in range(n - 1, k - 1, -1):
            a[j] = a[j] + r * a[j + 1]
    
    return a

result = compute_array(3, 0.5, [1, 2, 3, 4])
print(result)
