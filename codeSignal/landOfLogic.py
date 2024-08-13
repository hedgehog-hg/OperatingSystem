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

import numpy as np
def differentSquares(matrix):
    res = []
    square = np.array(matrix)
    for i in range(len(matrix)-1) :
        for j in range(len(matrix[0])-1):
            res.append(''.join(str(x) for x in square[i:i+2,j:j+2]))
    return len(set(res))

def digitsProduct(product):
    if product == 0:
        return 10
    res = []
    while product > 1 :
        for i in range(9,1,-1):
            if product%i == 0:
                res.append(i)
                product/=i
                break
        else : return -1
    return ''.join(sorted(res))

print(digitsProduct(450))
# print(differentSquares([[1, 2, 1],
#           [2, 2, 2],
#           [2, 2, 2],
#           [1, 2, 3],
#           [2, 2, 1]]))
#print(sumUpNumbers('three (3) is not 4'))
#print(validTime("13:58"))
#print(longestWord('Ready'))