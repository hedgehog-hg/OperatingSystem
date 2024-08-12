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

print(validTime("13:58"))
#print(longestWord('Ready'))