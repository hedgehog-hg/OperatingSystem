def isBeautifulStirng(inputString) :
    alpha = list(chr(97+i) for i in range(len(set(inputString))))
    print(alpha)
    cnt = inputString.count(alpha[0])
    for s in alpha:
        n_cnt = inputString.count(s)
        if n_cnt== 0 or cnt < n_cnt : return False
        cnt = n_cnt
    return True

def findEmailDomain(address):
    at= [idx for idx, x in enumerate(address) if x == '@']
    return address[at[-1]+1:]

def buildPalindrome(st):
    post =''
    for idx in range(len(st)-1):
        if st.count(st[idx]) > 1 and checkPalindrome(st[idx:]) :
            break
        else : 
            post += st[idx]
    return st+post[::-1]
def checkPalindrome(str):
    l = len(str)-1
    for i in range(len(str)//2) :
        if str[i] != str[l] :
            return False
        l-=1
    return True

print(buildPalindrome('abc'))
#print(findEmailDomain("\"very.unusual.@.unusual.com\"@usual.com"))
#print(isBeautifulStirng('zaa'))