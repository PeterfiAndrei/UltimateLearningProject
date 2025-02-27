
def isPalindrom(inputValue):
    if inputValue == int(str(inputValue)[::-1]):
        return True
    else:
        return False

print(isPalindrom(15233251))
print(isPalindrom(412))