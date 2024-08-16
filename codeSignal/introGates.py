def addTwoDigits(n):
    return n//10 + n%10
def largestNumber(n):
    return 10**n -1
def candies(n,m):
    return m//n *n
def seatsInTheater(nCols,nRows,col,row):
    return (nCols-col+1)*(nRows-row)
def maxMultiple(divisor,bound):
    return bound//divisor*divisor
def circleOfNumbers(n,firstNumber):
    mid = n//2
    return mid + firstNumber if firstNumber<mid else firstNumber%mid
def lateRide(n):
    h = n//60
    m = n-h*60
    return h//10 + h %10 + m//10 + m%10
def phoneCall(min1,min2_10,min11,s):
    if s >= min1 + 9*min2_10 : return 10 + (s-min1-9*min2_10)//min11
    elif s >= min1 : return 1 +(s-min1)//min2_10
    else : return 0
print(phoneCall(10,1,2,22))