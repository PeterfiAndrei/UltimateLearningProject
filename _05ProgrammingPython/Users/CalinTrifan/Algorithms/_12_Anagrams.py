def isAnagram(string1: str, string2: str) -> bool:
    string1 = string1.upper().replace(" ", "")
    string2 = string2.upper().replace(" ", "")

    string1 = sorted(string1)
    string2 = sorted(string2)

    if string1 == string2:
        return True
    else:
        return False


print(isAnagram("abcd cba", "badc     bac"))
