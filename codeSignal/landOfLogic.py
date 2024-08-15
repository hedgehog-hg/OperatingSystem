def longestWord(text):
    arr = []
    tmp = ''
    for c in text:
        if c.isalpha() :
            tmp += c
        else :
            arr.append(tmp)
            tmp = ''
    arr.append(tmp)
    return max(arr, key=lambda x: len(x))

def validTime(time) :
    h,m = map(int,time.split(':'))
    return 0<=h<24 and 0<=m<60

import re
def sumUpNumbers(inputString):
    return sum(int(x) for x in re.findall('\d+',inputString))

import numpy as np
def differentSquares(matrix):
    res = []
    square = np.array(matrix)
    for i in range(len(matrix)-1) :
        for j in range(len(matrix[0])-1):
            res.append(''.join(str(x) for x in square[i:i+2,j:j+2]))
    return len(set(res))

def digitsProduct(product):
    # product의 약수로 만들 수 있는 가장 작은 수 반환
    # 예시 ) product 450 일때 2559 반환
    # 약수는 0~9 사이의 값
    if product == 0:
        return 10
    res = []
    while product > 1 :
        # 9부터 내림 차순 ( 9로 나눠지면 3*3 도 가능 -> 33 보단 9 가 더 작다 )
        for i in range(9,1,-1): 
            if product%i == 0:
                res.append(i)
                product/=i
                break
        else : return -1
    return ''.join(sorted(res))

def fileNaming(names):
    res = []
    for i in range(len(names)):
        if names[i] in names[:i] or names[i] in res:
            cnt = res.count(names[i])
            tmp = names[i] + '(' + str(cnt) + ')'
            while tmp in res :
                cnt +=1
                tmp = names[i] + '(' + str(cnt) + ')'
            res.append(tmp)
        else :
            res.append(names[i])
    return res
def messageFromBinaryCode(code):
    return ''.join(chr(int(code[i:i+8],2)) for i in range(0,len(code),8))
def spiralNumbers(n):
    times = sorted([n] + [i for i in range(1,n)]*2,reverse=True)
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    res =[[0 for _ in range(n)] for _ in range(n) ]
    k=1
    i=idx=0
    j =-1
    for time in times :
        for _ in range(time):
            i,j = i+d[idx][0], j+d[idx][1]
            res[i][j] = k
            k+=1
        idx = (idx+1)%4
    return res
def sudoku(grid) :
    cmp = [i+1 for i in range(9)]
    for g in grid :
        if sorted(g) != cmp : return False
    for g in list(zip(*grid[::-1])) :
        if sorted(g) != cmp : return False
    idx = []
    for i in range(3) :
        for j in range(3) :
            idx.append((3*i,3*j))
    for start in idx :
        matrix = []
        for i in range(3) :
            for j in range(3) :
                matrix.append(grid[start[0]+i][start[1]+j])
        if cmp != sorted(matrix) : 
            return False
    return True


sample = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
print(sudoku(sample))
#print(spiralNumbers(5))
#sample = "010010000110010101101100011011000110111100100001"
#print(messageFromBinaryCode(sample))
# print(fileNaming(["doc", 
#  "doc", 
#  "image", 
#  "doc(1)", 
#  "doc"]))
#print(digitsProduct(450))
# print(differentSquares([[1, 2, 1],
#           [2, 2, 2],
#           [2, 2, 2],
#           [1, 2, 3],
#           [2, 2, 1]]))
#print(sumUpNumbers('three (3) is not 4'))
#print(validTime("13:58"))
#print(longestWord('Ready'))