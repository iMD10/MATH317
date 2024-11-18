def newton_method(f, f_, x, nmax, epsilon, delta):
    
    fx = f(x)
    print(0, x, fx)  # Initial output

    for n in range(1, nmax + 1):
        fp = f_(x)
        if abs(fp) < delta:
            print("small derivative")
            return
        
        d = fx / fp
        x = x - d
        fx = f(x)
        print(n, x, fx)  # Output after each iteration
        
        if abs(d) < epsilon:
            print("convergence")
            return
    return


def f(x):
    return x**3 -2*x**2 + x-3  # Function

def f_(x):
    return 3*x**2 - 4*x +1 # Derivative


newton_method(f, f_, x=3.0, nmax=20, epsilon=1e-6, delta=1e-6)

