import math

def sign(num):
    return int(math.copysign(1, num))

def f(x): # x^3 − 3x + 1
    return (x**3-3*x+1)

def y(x):
    return (x**3 - 2*x + 1 - x**2)

def bisection(f, a, b, nmax ,e):
    fa = f(a)
    fb = f(b)
    if sign(fa) == sign(fb):
        print(f"a = {a}, b = {b}, fa = {fa}, fb = {fb}")
        print("Function has same signs at a and b")
        return
    error = b - a
    for n in range(nmax+1):
        error = error/2
        c = a + error
        fc = f(c)
        print(f"n = {n}, c = {c}, fc = {fc}, error = {error}")
        if abs(error) < e:
            print("Convergence")
            return
        if sign(fa) != sign(fc):
            b = round(c,9)
            fb = round(fc,9)
        else:
            a = round(c,9)
            fa = round(fc,9)
    return


a = 0
b = 1
nmax = 20
# e = math.ulp(1.0)
e = 0.5e-6
bisection(y, a, b, nmax ,e)
