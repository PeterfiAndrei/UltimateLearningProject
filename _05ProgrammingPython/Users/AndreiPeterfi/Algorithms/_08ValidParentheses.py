def checkIfValidParentheses(inputString):
    if len(inputString) %2 != 0 or len(inputString) == 0:
        print("False0")
        return False

    for i in range(0,len(inputString),2):
        if inputString[i] != '(' and inputString[i] != '[' and inputString[i] != '{':
            print("False1")
            return False
        if inputString[i] == '(':
            if inputString[i+1] != ')':
                print("False2")
                return False

        if inputString[i] == '[':
            if inputString[i+1] != ']':
                print("False3")
                return False

        if inputString[i] == '{':
            if inputString[i+1] != '}':
                print("False4")
                return False
    return True


print(checkIfValidParentheses("()[]{}"))
