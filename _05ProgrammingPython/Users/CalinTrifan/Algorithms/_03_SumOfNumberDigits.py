def numberdigits(inputNumber):
    sum = 0

    while (inputNumber != 0):
        sum = sum + inputNumber % 10
        inputNumber = inputNumber // 10

    return sum


print("digits sum = ", numberdigits(3356))


def numberdigitsstring(inputNumber):
    return sum(int(digit) for digit in str(inputNumber))


print("digit character sum =", numberdigitsstring(432343))
