def growingPlant(upSpeed,downSpeed,desireHeight):
    # upSpeed : increase height fixed amount
    # downSpped : decrease height per every night
    # return days to reacht the " desiredHeight "
    day = 1
    while upSpeed*day - downSpeed*(day-1) < desireHeight :
        day +=1
    return day
def knapsackLight(v1,w1,v2,w2,maxW):
    items = sorted([[v1,w1],[v2,w2]],key=lambda x:-x[0])
    res = 0
    for item in items:
        if item[1] <= maxW : 
            res += item[0]
            maxW -= item[1]
    return res

def longestDigitsPrefix(inputString): 
    # not find the longest prefix each word.. just first one
    for idx, c in enumerate(inputString):
        if not c.isnumeric():
            return inputString[:idx]

def digitDegree(n):
    res = 0
    while n >= 10 :
        n = sum(int(s) for s in str(n))
        res += 1
    return res
print(digitDegree(91))
#print(longestDigitsPrefix("the output is 42"))
#print(knapsackLight(10,5,6,4,9))
#print(growingPlant(100,10,910))
