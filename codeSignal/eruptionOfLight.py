def isBeautifulStirng(inputString) :
    alpha = list(chr(97+i) for i in range(len(set(inputString))))
    print(alpha)
    cnt = inputString.count(alpha[0])
    for s in alpha:
        n_cnt = inputString.count(s)
        if n_cnt== 0 or cnt < n_cnt : return False
        cnt = n_cnt
    return True


print(isBeautifulStirng('zaa'))