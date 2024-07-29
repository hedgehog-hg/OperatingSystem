def circleOfNumbers(n,firstNumber):
    return firstNumber + (n//2)*(1 if n/2 > firstNumber else -1)

def depositProfit(deposit,rate,threshold):
    year = 0
    while deposit*(1+rate/100)**year < threshold:
        year+=1
    return year

def absoluteValuesSumMinimization(arr):
    size = len(arr)
    idx= size//2 -1 if size%2 == 0 else size//2
    return arr[idx]

import itertools
def stringsRearrangement(inputArray):
    for p in itertools.permutations(inputArray) :
        res = []
        # ('ab', 'bb', 'aa')
        for i in range(len(p)-1):
            cnt = 0
            # 'ab'&'bb' 'bb'&'aa'
            for pair in zip(p[i],p[i+1]):
                cnt += 1 if pair[0] != pair[1] else 0
            res.append(cnt)
        if all(diff == 1 for diff in res) : return True
    return False

#print(circleOfNumbers(6,3))
#print(depositProfit(100,20,170))
#print(absoluteValuesSumMinimization([2,4,7]))
print(stringsRearrangement(['ab','bb','aa']))