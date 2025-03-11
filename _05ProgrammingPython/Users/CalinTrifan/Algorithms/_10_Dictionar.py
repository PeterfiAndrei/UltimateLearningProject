def countLetterts(inputstring):
    letters = {}

    for i in range(len(inputstring)):
        if inputstring[i] != " " and inputstring[i].isalpha():
            letters[inputstring[i]] = 1 + letters.get(inputstring[i], 0)

    return dict(sorted(letters.items()))


print(countLetterts("abaac ss r  # 3 w3 45 rg "))
