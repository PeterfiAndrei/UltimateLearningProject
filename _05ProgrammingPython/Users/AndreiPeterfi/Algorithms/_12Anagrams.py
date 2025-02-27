def isAnagram(firstString, secondString):
    firstString = str(firstString).lower().replace(" ","")
    secondString = str(secondString).lower().replace(" ","")
    return sorted(firstString) == sorted(secondString)


print(isAnagram("a adi","iada"))