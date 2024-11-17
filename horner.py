# Horner’s algorithm
# (n) is the power of the polynomial, (r) is the value at which you want to evaluate the polynomial
# (a) is an array of p(r) coefficients, (b) is an array of n-1 size for calculations
def horner_algorithm(a,r):
    n = len(a)-1 # power of the polynomial
    b = list(range(n)) # array of n-1 size for calculations "Contents dose not matter now"
    b[n-1] = a[n]

    print("p(r) = ",end='') # prints the polynomial function
    if a[0] < 0:
        print(" - ",end='') 
    for i in range(n+1):
        print(f"{abs(a[i])}x^{i}",end='')
        if i != n:  
            if a[i+1]>=0:
                print(" + ",end='')
            else:
                print(" - ",end='') 

    for i in range(n-1,-1,-1):
        b[i-1] = a[i] + r * b[i]
    print(f"\np({r}) = {b[-1]}")
    # Notice that b[−1] = p(r) 

horner_algorithm([-2,-5,7,-4,1],3)
# Notice that p(x) coefficients are entered in this way
# representing x^4 - 4x^3 + 7x^2 -5x - 2