def killKthBit(n,k):
    # n the Kth bit 0
    return n & ~(1 << (k - 1))
def arrayPacking(a):
    return int(''.join(list(format(n,'b').zfill(8)for n in a)[::-1]),2)
def rangeBitCount(a,b):
    return sum(bin(i).count('1') for i in range(a,b+1))
def mirrorBits(a):
    return int(bin(a)[2:][::-1],2)
print(mirrorBits(97))
#print(rangeBitCount(2,7))
#print(arrayPacking([24,85,0]))
#print(killKthBit(37,4))