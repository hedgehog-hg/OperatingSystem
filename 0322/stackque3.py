
def sol(s) :
    stk = []
    for bracket in s :
        if bracket == '(':
            stk.append(bracket)
        else:
            if not stk : return False
            stk.pop()
    return not stk

# input data
s = ")()()"
print(sol(s))

