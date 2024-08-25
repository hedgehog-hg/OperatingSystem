def killKthBit(n,k):
    # n the Kth bit 0
    return n & ~(1 << (k - 1))

# 100101
# 
print(killKthBit(37,4))