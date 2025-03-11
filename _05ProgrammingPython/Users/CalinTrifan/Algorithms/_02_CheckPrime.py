def checkPrime(inputValue):
    if inputValue <= 1:
        return False
    if inputValue == 2:
        return True
    for i in range(3, int(inputValue**0.5), 2):
        if inputValue % i == 0:
            return False

    return True


print(checkPrime(71))
