def isPrime(inputNumber):
    if inputNumber == 2:
        return True
    elif inputNumber<=1 or inputNumber % 2 == 0 :
        return False
    else:
        for i in range(3,int(inputNumber ** 0.5+1),2):
            if inputNumber % i == 0:
                print("False because", inputNumber, "is divided by", i)
                return False
        return True

print(isPrime(723))