def areEquallyStrong(yourLeft,yourRight,friendsLeft,friendsRight) :
    return sorted([yourLeft,yourRight]) == sorted([friendsLeft,friendsRight])

def arrayMaximalAdjacentDifference(inputArray):
    diff = list(abs(inputArray[i]-inputArray[i+1]) for i in range(len(inputArray)-1))
    return max(diff)

import re
def isIPv4Address(inputString):
    address = inputString.split('.')
    if len(address) != 4 : return False
    notNumber = re.compile('[^0-9]')
    leadingZero = re.compile('0[0-9]+')
    for add in address : 
        if add == '' : return False
        if notNumber.search(add) : return False
        if leadingZero.match(add) : return False
        if int(add) < 0 or int(add) > 255 : return False
    return True

import re
def isIPv4(inputString) :
    address = inputString.split('.')
    leadingZero = re.compile('0\d+')
    return len(address) == 4 and all(n.isdigit() and not leadingZero.search(n) and 0 <= int(n) <= 255 for n in address)

def avoidObstacles(inputArray):
    jump = 2
    while not all(n%jump for n in inputArray) : 
        jump +=1
    return jump

import numpy as np, math
def boxBlur(image):
    # n * m matrix
    n = len(image)-2
    m = len(image[0])-2
    res=[]
    for i in range(n) :
        sum_arr = []
        for j in range(m):
            sum_arr.append(math.floor(np.sum(list(image[i+n][j:j+3] for n in range(3)))/9))    
        res.append(sum_arr)
    return res

def minesweeper(matrix):
    # 자신 제외 주변에 true = 지뢰 있으면 +1
    # leftup up rightup
    # left   idx right
    # leftdown down rightdown
    res = []
    for i in range(len(matrix)):
        arr = []
        for j in range(len(matrix[i])):
            left = leftOrup(j-1)
            right= rightorDown(j+1,len(matrix[i]))
            up = leftOrup(i-1)
            down = rightorDown(i+1,len(matrix))
            arr.append(sum([left and up and matrix[i-1][j-1], up and matrix[i-1][j], right and up and matrix[i-1][j+1],
            left and matrix[i][j-1], right and matrix[i][j+1],
            left and down and matrix[i+1][j-1], down and matrix[i+1][j], right and down and matrix[i+1][j+1]]))
        res.append(arr)
    return res
def leftOrup(idx) :
    return True if idx>=0 else False
def rightorDown(idx,size) :
    return True if idx < size else False



#print(areEquallyStrong(10,15,15,10))
#print(arrayMaximalAdjacentDifference([2,4,1,0]))
#print(isIPv4("1.255.254.00"))
#print(avoidObstacles([1,10]))
# print(boxBlur([[36,0,18,9], 
#  [27,54,9,0], 
#  [81,63,72,45]]
# ))
print(minesweeper([[True, False, False],
          [False, True, False],
          [False, False, False]]))