def checkIfValidParanthese(inputString):
    if len(inputString) % 2 != 0:
        return False
    str1 = "()"
    str2 = "[]"
    str3 = "{}"
    for i in range(0, len(inputString), 2):
        subString = inputString[i : i + 2]
        if str1 != subString and str2 != subString and str3 != subString:
            return False
    return True


print(checkIfValidParanthese("()[]{}"))
