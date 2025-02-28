def reverseNumber(numberToRevers):
    reversedNumber = 0

    while (numberToRevers != 0):
        reversedNumber = (reversedNumber * 10) + numberToRevers % 10
        numberToRevers = numberToRevers // 10

    return reversedNumber


def reverseNumber2(inputNumber):
    return ((str(inputNumber)[::-1]))


print("revers number is :", reverseNumber(345))
print("revers number is :", reverseNumber2("abcd"))
