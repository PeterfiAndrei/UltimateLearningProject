def removeDuplicateElements(inputList: list):
    finalList = []
    for element in inputList:
        if element not in finalList:
            finalList.append(element)
    return finalList


initialList = ["Calin", "Andrei", "Andrei", "Laura", "Denisa", "Marius"]
finalList = removeDuplicateElements(initialList)
print("Lista finala:", finalList)
finalList[1] += "2"

print(finalList[1])
finalList.pop(1)
finalList.sort(reverse=True)
print(finalList)

coordonate = (42, 23)
coordonate = (41, 10)
coordonate[0] = 12
print(coordonate)
