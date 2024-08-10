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

print(lineEncoding('aabbbc'))
#print(isDigit('0'))