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

def boxBlur(image):
    return 
#print(areEquallyStrong(10,15,15,10))
#print(arrayMaximalAdjacentDifference([2,4,1,0]))
#print(isIPv4("1.255.254.00"))
#print(avoidObstacles([1,10]))
print(boxBlur([[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]))