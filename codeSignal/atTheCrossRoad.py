def reachNextLevel(experience,threshold,reward):
    return experience + reward >= threshold
def knapsackLight(value1,weight1,value2,weight2,maxW):
    if weight1 + weight2 <= maxW :
        return value1 + value2
    else :
        arr =[]
        if weight1 <= maxW :
            arr.append(value1)
        if weight2 <= maxW :
            arr.append(value2)
        return max(arr) if arr else 0

print(knapsackLight(10,2,11,3,1))
#print(reachNextLevel(10,15,5))