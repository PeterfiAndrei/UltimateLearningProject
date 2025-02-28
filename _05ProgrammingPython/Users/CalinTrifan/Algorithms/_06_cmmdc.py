def cmmdc(value1, value2):
    if value1 > value2:
        value1, value2 = value2, value1

    max = 1
    for i in range(2, value1 + 1, 1):
        if value1 % i == 0 and value2 % i == 0:
            max = i

    return max


if __name__ == "__main__":
    print("cmmdc =", cmmdc(4, 8))
