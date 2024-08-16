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