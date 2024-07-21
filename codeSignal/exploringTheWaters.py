def alternatingSums(a):
    res = [0,0]
    for idx,w in enumerate(a) :
        res[idx%2] += w
    return res

print(alternatingSums([50,60,60,45,70]))
