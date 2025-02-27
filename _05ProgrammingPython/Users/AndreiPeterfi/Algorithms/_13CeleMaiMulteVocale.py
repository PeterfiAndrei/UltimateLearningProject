def findMostVowels(inputText: str) -> str:
    words = (
        inputText.split()
    )  # Default e spatiu, dar se poate da orice caracter sau string. separatorul va fi exclus
    longestWord = ""
    maxVowels = 0
    for word in words:
        currentNoOfWords = 0
        for i in range(len(word)):
            if word[i].lower() in "aeiou":
                currentNoOfWords += 1
        if currentNoOfWords > maxVowels:
            maxVowels = currentNoOfWords
            longestWord = word
    return longestWord


print(
    "The word with the most vowels is:", findMostVowels("aceasta e o propozitie lunga")
)
