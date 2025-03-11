def checkifvalidpharantesses(inputString):
    if len(inputString) % 2 != 0:
        return False

    countParantesses1 = 0  # ()
    countParantesses2 = 0  # []
    countParantesses3 = 0  # {}

    for i in range(0, len(inputString), 1):
        if inputString[i] == "(":
            countParantesses1 = countParantesses1 + 1
        if inputString[i] == ")":
            countParantesses1 = countParantesses1 - 1
        if inputString[i] == "[":
            countParantesses2 = countParantesses2 + 1
        if inputString[i] == "]":
            countParantesses2 = countParantesses2 - 1
        if inputString[i] == "{":
            countParantesses3 = countParantesses3 + 1
        if inputString[i] == "}":
            countParantesses3 = countParantesses3 - 1

        if countParantesses1 < 0 or countParantesses2 < 0 or countParantesses1 < 0:
            return False

    if countParantesses1 == 0 and countParantesses2 == 0 and countParantesses3 == 0:
        return True
    else:
        return False


print(checkifvalidpharantesses("()[]{}"))

print(checkifvalidpharantesses("(()[]{})"))

print(checkifvalidpharantesses("([)]"))
