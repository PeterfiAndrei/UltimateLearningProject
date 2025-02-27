def sumOfNumberDigits(inputNumber):
    sum =0
    while inputNumber > 0:
        sum += int(inputNumber % 10)
        inputNumber //= 10          ##Folosind dubla impartire va returna valoare intreaga
        print(sum)
    return sum


def sumOfDigitsString(inputValue):
    return sum(int(digit) for digit in str(inputValue))


print("Suma elementelor numarului 236124:",sumOfNumberDigits(236124))
print("Varianta cu String:",sumOfDigitsString(236124))

