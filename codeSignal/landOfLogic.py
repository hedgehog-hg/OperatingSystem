def longestWord(text):
    arr = []
    tmp = ''
    for c in text:
        if c.isalpha() :
            tmp += c
        else :
            arr.append(tmp)
            tmp = ''
    arr.append(tmp)
    return max(arr, key=lambda x: len(x))

def validTime(time) :
    h,m = map(int,time.split(':'))
    return 0<=h<24 and 0<=m<60

import re
def sumUpNumbers(inputString):
    return sum(int(x) for x in re.findall('\d+',inputString))

print(sumUpNumbers('three (3) is not 4'))
#print(validTime("13:58"))
#print(longestWord('Ready'))