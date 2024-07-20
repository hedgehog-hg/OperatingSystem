def allLongestStrings(inputArray):
    res = []
    longest = len(inputArray[0])
    for arr in inputArray:
        cur_len = len(arr)
        if cur_len > longest:
            res=[arr]
            longest=cur_len
        elif cur_len == longest :
            res.append(arr)

    return res

def commonCharacterCount(s1,s2) :
    s1_char = {}
    for s in set(s1) :
        s1_char[s] = s1.count(s)
    sum = 0
    for s in set(s2) :
        if s in s1 :
            sum+=min(s1_char[s],s2.count(s))

    return sum

def isLucky(n):
    arr = list(map(int,list(str(n))))
    return sum(arr[:len(arr)//2]) == sum(arr[len(arr)//2:])

def sortHeight(a):
    sorted_a = sorted(a)
    idx = a.count(-1)
    for i in range(len(a)) :
        if a[i] == -1 : continue
        a[i] = sorted_a[idx]
        idx+=1
    return a

def reverseInParentheses(inputString):
    res = ""
    stk = []
    for idx,s in enumerate(inputString) :
        res += s
        if s == '(' : stk.append(idx)
        elif s == ')' :
            start = stk.pop()+1
            res = res[:start] + res[start:idx+1][::-1]
            
            
    return res.replace('(','').replace(')','')
#print(allLongestStrings(["aba","aa","ad","vcd","aba"]))
#print(commonCharacterCount("aabcc","adcaa"))
#print(isLucky(1230))
#print(sortHeight([-1, 150, 190, 170, -1, -1, 160, 180]))
print(reverseInParentheses("foo(bar)baz(blim)"))