def leastFactorial(n):
    f = 1
    k = 2
    while f<n:
        f*=k
        k+=1
    return f