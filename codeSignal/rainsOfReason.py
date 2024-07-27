def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return list(substitutionElem if n == elemToReplace else n for n in inputArray)

def evenDigitsOnly(n):
    return all(int(n)%2 == 0 for n in str(n))


def variableName(name) :
    return not name[0].isdigit() and all(n.isalpha() or n == '_' or n.isdigit() for n in name)

def alphabeticShift(inputString):
    return ''.join(chr(ord(s)+1) if s!='z' else 'a' for s in inputString)

def chessBoardCellColor(cell1,cell2):
    return not((ord(cell1[0])+int(cell1[1])) % 2 ^ (ord(cell2[0])+int(cell2[1]))%2)
#print(arrayReplace([1,2,1],1,3))
#print(evenDigitsOnly(248622))
#print(variableName('var_1_INT'))
#print(alphabeticShift('crazy'))
print(chessBoardCellColor('A1','C3'))