def isDigit(symbol):
    return all(s.isdigit() for s in symbol)

print(isDigit('0'))