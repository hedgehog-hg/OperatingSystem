def solution(operations) :
    que = []
    for operation in operations :
        o = operation.split()
        if o[0] == "I" :
            que.append(int(o[1]))
        else :
            if que and o[1] == '1' : # delete maximum
                que.pop(que.index(max(que)))
            elif que and o[1] == '-1' : # delete minimum
                que.pop(que.index(min(que)))

    if not que : 
        return [0,0]
    return [max(que),min(que)]

#input data
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))
