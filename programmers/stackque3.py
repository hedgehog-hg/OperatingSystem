
def sol(s) :
    stk = []
    for bracket in s :
        if bracket == '(':
            stk.append(bracket)
        else:
            try :
                stk.pop()
            except IndexError :
                return False
    return not stk

# input data
s = ")()()"
print(sol(s))

