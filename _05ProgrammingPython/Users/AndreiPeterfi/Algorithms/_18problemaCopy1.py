import copy


def duplicateInputString(inputString: str):
    inputString = inputString + inputString

    print(inputString)


def changeListFirstElement(inputList):
    # inputList1 = copy.deepcopy(inputList)

    # inputList1[0]="zz"
    inputList1 = inputList
    inputList1[0] = "zz"
    print(inputList1)


if __name__ == "__main__":
    print("aici")

    nume = "Trifan"
    duplicateInputString(nume)  # TrifanTrifan
    print(nume)  # TrifanTrifan

    lista = ["ioana", "miha", "andreo", "geo"]
    changeListFirstElement(lista)  # zz miha anrei geo
    print(lista)  # ioana","miha","andreo","geo
