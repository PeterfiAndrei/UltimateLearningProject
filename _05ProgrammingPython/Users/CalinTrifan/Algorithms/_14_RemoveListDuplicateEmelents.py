def removeDuplicateElements(lista: list):
    finalList = []
    for element in lista:
        if element not in finalList:
            finalList.append(element)

    return finalList


listaInitiala = ["eu", "tu", "eu", "el", "voi", "noi", "toti"]

print("lista fara dubplicate este :", removeDuplicateElements(listaInitiala))
print(sorted(removeDuplicateElements(listaInitiala), reverse=True))
