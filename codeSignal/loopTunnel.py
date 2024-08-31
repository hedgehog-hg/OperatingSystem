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
def lineup(commands):
    l = 1
    r = 1
    cnt =0
    for order in commands:
        if order =='L':
            l*=1
            r*=-1
        elif order =='R':
            l*=-1
            r*=1
        if l == r : cnt+=1

    return cnt
def additionWithoutCarrying(param1,param2):
    res =''
    while param1 or param2 :
        res += str(param1%10 + param2%10)[-1]
        print(res)
        param1 = param1//10
        param2 = param2//10
    return int(res[::-1]) if res else 0

print(additionWithoutCarrying(456,1734))
#print(lineup('LLARL'))
#print(magicalWell(6,5,3))
#print(countSumOfTwoRepresent(6,2,4))