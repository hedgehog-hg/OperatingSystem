def add(param1, param2) :
 return param1 + param2

import math
def centuryFromYear(year) :
   return math.ceil(year/100)

def checkPalindrom(inputString) :
    length = len(inputString)
    for i in range(length) :
        if inputString[i] != inputString[length-1-i] :
            return False
    return True

print(checkPalindrom("abac"))
