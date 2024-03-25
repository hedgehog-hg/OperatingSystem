import math
def sol(prog, speeds) :
    dstack = []
    for i in range(len(prog)) :
        dstack.append(math.ceil((100-prog[i])/speeds[i]))
    ans = []
    pivot = 0
    cnt = 0
    for i in range(len(dstack)) :
        if dstack[pivot] >= dstack[i] :
            cnt+=1
        else :
            pivot = i+1
            ans.append(cnt)
            cnt = 1
    ans.append(cnt)
    return ans

# input data
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(sol(progresses,speeds))

