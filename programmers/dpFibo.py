# top-down
def fib(n) :
    if f[n]!=0 : return f[n]
    if n in (1,2) : f[n] = 1
    else :
        f[n] = fib(n-1) + fib(n-2)
        return f[n]

# bottom-up
def fibonacci(n) :
    f=[0 for _ in range(n+1)]
    f[1] = 1
    f[2] = 1
    for i in range(3,n+1) :
        f[i] = f[i-1]+f[i-2]
    return f[n]

# f = [0 for i in range(100)]
# print(fib(int(input())))

print(fibonacci(int(input())))