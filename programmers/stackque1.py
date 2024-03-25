def sol(arr) :
    ans = [arr[0]]
    for n in arr :
        if ans[-1] != n :
            ans.append(n)
    return ans


sample = [4,4,4,3,3]
print(sol(sample))