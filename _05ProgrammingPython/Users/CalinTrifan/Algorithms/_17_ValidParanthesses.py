def checkifvalidpharantesses(inputString):
    # Definim o stivă
    stack = []

    # Maparea parantezelor de închidere la parantezele de deschidere
    parantheses_map = {")": "(", "]": "[", "}": "{"}
    #  parantheses_map = {"(": ")", "[": "]", "{": "}"}

    for char in inputString:
        # Daca gasim o paranteză de deschidere, o adaugăm în stiva
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            # Daca gasim o paranteză de închidere, verificăm daca exista
            # o paranteza corespunzătoare la varful stivei
            if stack[-1] == parantheses_map[char]:
                stack.pop()  # inlaturam paranteza de deschidere corespunzatoare
            else:
                return False  # Daca nu se potriveste, nu e valid

    # Daca stiva este goala, toate parantezele s-au închis corect
    return len(stack) == 0


# Testare
print(checkifvalidpharantesses("()[]{}"))  # True
print(checkifvalidpharantesses("([)]"))  # False
print(checkifvalidpharantesses("{[()]}"))  # True
print(checkifvalidpharantesses("{[()}]"))
