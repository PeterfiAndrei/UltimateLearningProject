def checkpalindrom(inputNumber):
    if int((str(inputNumber)[::-1])) == inputNumber:
        return True
    else:
        return False


print(checkpalindrom(349))
