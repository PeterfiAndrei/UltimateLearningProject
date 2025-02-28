def checkifvalidpharantesses(inputString):
    if len(inputString) % 2 != 0:
        return False
    str1 = "()"
    str2 = "[]"
    str3 = "{}"
    for i in range(0, len(inputString), 2):
        substring = inputString[i:i + 2]
        print("substring", substring)
        if str1 != substring and str2 != substring and str3 != substring:
            return False

    return True


print(checkifvalidpharantesses("()[]"))
