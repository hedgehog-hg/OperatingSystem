def isDigit(symbol):
    return all(s.isdigit() for s in symbol)

def lineEncoding(s):
    res = ''
    prv = ''
    cnt = 0
    for c in s :
        if prv and prv != c :
            if cnt > 1 : res += str(cnt)
            res += prv
            cnt = 1
        if not prv or prv == c :
            cnt += 1
        prv = c
    if cnt > 1 : res += str(cnt)
    return res + prv

def chessKnight(cell):
    a = ord(cell[0])
    n = int(cell[1])
    canGo = [ [a-2,n-1],[a-2,n+1],[a-1,n-2],[a-1,n+2],[a+1,n+2],[a+1,n-2],[a+2,n+1],[a+2,n-1]]
    return sum(checkValidAlpha(chr(g[0])) and checkValidNum(g[1]) for g in canGo)
def checkValidAlpha(x) :
    return 'a' <= x <= 'h'
def checkValidNum(n) :
    return 0 < n < 9

def deleteDigit(n):
    st = str(n)
    return int(max(st[:i] + st[i+1:] for i in range(len(st))))




print(deleteDigit(152))
#print(chessKnight('a1'))
#print(lineEncoding('aabbbc'))
#print(isDigit('0'))