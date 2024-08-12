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
print(longestWord('Ready'))