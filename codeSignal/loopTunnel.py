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

print(countSumOfTwoRepresent(6,2,4))