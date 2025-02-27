def countLetters (inputString):
    letters = {}
    #letters["a",0]
    for i in range(len(inputString)):
        if inputString[i]!=" " and inputString[i].isalpha():
            letters[inputString[i].lower()] = letters.get(inputString[i].lower(),0) + 1

    return dict(sorted(letters.items()))



print(countLetters(" blAn a3$4"))
