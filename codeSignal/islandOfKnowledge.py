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

#print(areEquallyStrong(10,15,15,10))
#print(arrayMaximalAdjacentDifference([2,4,1,0]))
print(isIPv4Address("1a.255.254.0"))