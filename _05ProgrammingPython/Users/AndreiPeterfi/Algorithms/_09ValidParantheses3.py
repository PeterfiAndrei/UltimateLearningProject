def checkIfValidParanthese(inputString):
    if len(inputString) % 2 != 0:
        return False
    countParantheses1 = 0       #()
    countParantheses2 = 0       #[]
    countParantheses3 = 0       #{}

    for i in range (len(inputString)):
        if inputString[i] == '(':
            countParantheses1 += 1
        if inputString[i] == ')':
            countParantheses1 -= 1
        if inputString[i] == '[':
            countParantheses2 += 1
        if inputString[i] == ']':
            countParantheses2 -= 1
        if inputString[i] == '{':
            countParantheses3 += 1
        if inputString[i] == '}':
            countParantheses3 -= 1
        if countParantheses1 < 0 or countParantheses2 < 0 or countParantheses3 < 0:
            return False

    if countParantheses1 == 0 and countParantheses2 == 0 and countParantheses3 == 0:
        return True
    else:
        return False

print(checkIfValidParanthese("()a[]{}"))