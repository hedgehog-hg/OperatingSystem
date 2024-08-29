def leastFactorial(n):
    f = 1
    k = 2
    while f<n:
        f*=k
        k+=1
    return f
import math
def countSumOfTwoRepresent(n,l,r):
    return math.ceil(len(set(sum(list([i,n-i] for i in range(l,r+1) if l<=n-i <= r),[])))/2)
def magicalWell(a,b,n):
    print((n-1)*(a+b))
    return n*a*b + sum(range(n))*(a+b) + sum(i**2 for i in range(1,n))

print(magicalWell(6,5,3))
#print(countSumOfTwoRepresent(6,2,4))