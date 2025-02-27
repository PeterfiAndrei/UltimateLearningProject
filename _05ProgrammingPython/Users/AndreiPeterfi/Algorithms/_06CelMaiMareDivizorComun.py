def cmmdc(firstValue, secondValue):
    if firstValue<secondValue:
        firstValue,secondValue = secondValue,firstValue

    for i in range(secondValue, 0, -1):
        if firstValue % i == 0 and secondValue % i == 0:
            return i
    return 1

if __name__ == "__main__":                  #Pentru a evita executia la import
    print(cmmdc(9,27))