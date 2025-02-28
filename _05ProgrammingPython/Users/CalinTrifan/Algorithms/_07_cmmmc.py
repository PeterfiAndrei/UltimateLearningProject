from _06_cmmdc import cmmdc


def cmmmc(value1, value2):
    # print("abs result:",abs(value1*value2))
    # print("cmmdc result:",cmmdc(value1,value2))
    return abs(value1 * value2) // cmmdc(value1, value2)


print("cmmmc=", cmmmc(4, 8))
