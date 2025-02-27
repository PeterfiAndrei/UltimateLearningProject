def checkEcuatieGrad2(inputText: str):
    print(f"Initial ecuation: {inputText}")
    split = inputText.split("x")
    a = 1
    try:
        a = int(split[0])
    except ValueError:
        a = 1
    b = int(split[1][2:])
    c = int(split[2].split("=")[0])
    print(f"a = {a} b= {b} c= {c}")
    delta = b**2 - 4 * a * c
    # print(f"delta = {delta}")
    if delta == 0:
        # print("Vom printa un numar")
        finalResult = -1 * b / (2 * a)
        return finalResult
    if delta > 0:
        # print("vom afla cele 2 numere si le returnam ca tuple")
        result1 = (-1 * b + delta**0.5) / (2 * a)
        result2 = (-1 * b - delta**0.5) / (2 * a)
        return {int(result1), int(result2)}
    if delta < 0:
        # print("No solutions")
        return "No solutions"


print(f"the solution is: {checkEcuatieGrad2('x^2+3x-70=0')}")
print(f"the solution is: {checkEcuatieGrad2('2x^2-4x-6=0')}")
print(f"the solution is: {checkEcuatieGrad2('0.5x^2-2x+2=0')}")
