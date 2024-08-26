def killKthBit(n,k):
    # n the Kth bit 0
    return n & ~(1 << (k - 1))
def arrayPacking(a):
    return int(''.join(list(bin(n)[2:]for n in a)[::-1]),2)
print(arrayPacking([24,85,0]))
#print(killKthBit(37,4))