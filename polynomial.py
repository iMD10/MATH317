# polynomial Evaluation
# (arr) is a real array, (n) is the power of the polynomial, (x) represents the argument of the polynomial function
def polynomial_Evaluation(arr,x): 
    n = len(arr)-1 # power of the polynomial
    p = arr[n]

    print("p(x) = ",end='') # prints the polynomial function
    if arr[0] < 0:
        print(" - ",end='') 
    for i in range(n+1):
        print(f"{abs(arr[i])}x^{i}",end='')
        if i != n:  
            if arr[i+1]>=0:
                print(" + ",end='')
            else:
                print(" - ",end='') 

    for i in range(n-1, -1, -1): # calculates p(x)
        p = arr[i] + x * p
    print(f'\np({x}) = ',p)

polynomial_Evaluation([3,-2,4,-7,1],5)