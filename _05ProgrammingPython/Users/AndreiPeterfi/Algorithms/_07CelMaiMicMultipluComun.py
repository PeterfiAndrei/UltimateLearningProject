from _06CelMaiMareDivizorComun import cmmdc

def celMaiMicMultipluComun(firstValue, secondValue):
    firstValue,secondValue = abs(firstValue),abs(secondValue)
    if firstValue == 0 or secondValue == 0:
        return 0
    return firstValue * secondValue // cmmdc(firstValue,secondValue)

print("Cel mai mic multiplu comun e:",celMaiMicMultipluComun(-27,3))