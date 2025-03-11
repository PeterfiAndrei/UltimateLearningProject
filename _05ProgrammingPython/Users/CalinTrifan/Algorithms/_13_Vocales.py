def getWordWIthMostVocals(string1: str):
    cuvinte = string1.split(" ")
    max = 0
    longest_word = ""
    for cuvant in cuvinte:
        currentCount = 0
        for litera in range(len(cuvant)):
            if cuvant[litera] in "aeiouAEIOU":
                currentCount = currentCount + 1
        if max < currentCount:
            max = currentCount
            longest_word = cuvant

    return longest_word


print("Cuvantul cu cele mai multe vocale este:", getWordWIthMostVocals("Aceasta este o prOpOzitie de test"))
