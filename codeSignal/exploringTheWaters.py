def alternatingSums(a):
    res = [0,0]
    for idx,w in enumerate(a) :
        res[idx%2] += w
    return res

def alternatingSums_simple(a) :
    return [sum(a[::2]),sum(a[1::2])]

def addBorder(picture):
    res=[]
    for sen in picture :
        res.append("*{}*".format(sen))
    frame = "*"*len(res[0])
    res.insert(0,frame)
    res.append(frame)
    return res

def areSimilar(a,b):
    # a is equal to b by swapping at most one pair 
    diff = sum(i!=j for i,j in zip(a,b)) < 3
    return sorted(a) == sorted(b) and diff

def arrayChange(inputArray):
    sum = 0
    for i in range(len(inputArray)-1) :
        if inputArray[i] >= inputArray[i+1] :
            inc = inputArray[i] - inputArray[i+1] + 1
            inputArray[i+1] += inc
            sum += inc 
    return sum

def palindromeRearranging(inputString):
    return sum(inputString.count(s) % 2 != 0 for s in set(inputString)) <2

#print(alternatingSums_simple([50,60,60,45,70]))
#print(addBorder(["abc","ded"]))
#print(areSimilar([1,2,1,2],[2,2,1,1]))
#print(arrayChange([1,1,1]))
print(palindromeRearranging('aacbb'))
