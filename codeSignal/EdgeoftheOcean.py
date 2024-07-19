def adjacentElementsProduct(inputArray) :
    product= []
    for i in range(len(inputArray)-1) :
        product.append(inputArray[i]*inputArray[i+1])
    return max(product)

def shapeArea(n) :
    return n**2 + (n-1)**2

def makeArrayConsecutive(statues):
    return max(statues) - min(statues) +1 -len(statues)

def almostIncreasingSequence(sequence):
    dcs = []
    for i in range(len(sequence)-1) :
        if sequence[i] >= sequence[i+1] : 
            if dcs : return False
            dcs = [i,i+1]
    if not dcs : return True
    else :
        prev = dcs[0] -1
        next = dcs[1] +1
        if prev >= 0 : 
            for d in dcs :
                if sequence[prev] >= sequence[d] : dcs.remove(d)
        if dcs and next != len(sequence) :
            for d in dcs :
                if sequence[next] <= sequence[d] : dcs.remove(d)
        if dcs : return True
            
        return False

def matrixElementsSum(matrix) :
    ghost = []
    sum = 0
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :
            if j in ghost : continue
            if matrix[i][j] == 0 :
                ghost.append(j)
            sum += matrix[i][j]
    return sum


#print(adjacentElementsProduct([3,6,-2,-5,7,3]))
#print(shapeArea(2))
#print(makeArrayConsecutive([6,2,3,8]))
sample = [1,1,2,3,4,4]
#print(almostIncreasingSequence(sample))
ms = [[1,1,1,0], 
 [0,5,0,1], 
 [2,1,3,10]]
print(matrixElementsSum(ms))
