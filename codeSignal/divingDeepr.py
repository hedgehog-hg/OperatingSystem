def extractEachKth(inputArray,k):
    return list(n for idx,n in enumerate(inputArray) if (idx+1)%k!=0 )

def firstDigit(inputString):
    for s in inputString :
        if s.isdigit() : return s
    return 'no digit'
    

#print(extractEachKth([1,2,3,4,5,6,7,8,9,10],3))
print(firstDigit('var_1__Int'))