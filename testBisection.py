def f(x):
    return x**3 - 3*x + 1

def g(x):
    from math import sin
    return x**3 - 2 * sin(x)

def bisection(func, a, b, nmax, epsilon):
   
    fa = func(a)
    fb = func(b)

    if fa * fb >= 0:
        print(f"a = {a}, b = {b}, fa = {fa}, fb = {fb}")
        print("Function has the same signs at a and b")
        return None

    error = b - a
    print(f"{'n':<5} {'c_n':<15} {'f(c_n)':<15} {'error':<15}")
    print("-" * 50)

    for n in range(nmax+1):
        error = error / 2
        c = a + error
        fc = func(c)

        
        print(f"{n:<5} {c:<15.8f} {fc:<15.8e} {error:<15.8e}")

        if abs(error) < epsilon:
            print("Convergence")
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    print("Max iterations reached.")
    return None


nmax = 20
epsilon = 0.5 * 10**-6

# First test case with function f
a = 0.0
b = 1.0
print("\nBisection Method for f(x) = x^3 - 3x + 1 on [0.0, 1.0]")
bisection(f, a, b, nmax, epsilon)

# Second test case with function g
a = 0.5
b = 2.0
print("\nBisection Method for g(x) = x^3 - 2*sin(x) on [0.5, 2.0]")
bisection(g, a, b, nmax, epsilon)
