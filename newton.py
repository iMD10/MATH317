def newton_method(f, f_, x, nmax, epsilon, delta):
    
    """
    Newton-Raphson method for finding roots of a function.
    
    Parameters:
    f : callable
        The function for which the root is to be found.
    f_: callable
        The derivative of the function.
    x : float
        The initial guess for the root.
    nmax : int
        The maximum number of iterations.
    epsilon : float
        The tolerance for convergence.
    delta : float
        The tolerance for small derivatives.

    Returns:
    None
    """
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

