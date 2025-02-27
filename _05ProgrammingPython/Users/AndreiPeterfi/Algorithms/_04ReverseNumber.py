def reverse_number(inputValue):
    finalValue = 0
    while inputValue > 0:
        finalValue = finalValue * 10 + inputValue % 10
        inputValue //= 10
    return finalValue


def reverse_number_using_string(inputValue):
    return int(str(inputValue)[::-1])  #### [::-1] e folosit pentru a inversa un string]


print(reverse_number(1251))
print(reverse_number_using_string(1251))
