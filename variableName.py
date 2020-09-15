# Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.^
import re
def variableName(name):
    isValidVariable = True
    containLetters = re.findall('[a-zA-Z]', name[0])
    containUnderscore = re.findall('_', name[0])
    containSpace = re.findall('\s', name)
    otherChars = re.findall('([^a-zA-Z0-9_])', name)
    if not(containLetters) and not(containUnderscore):
        isValidVariable = False
        return isValidVariable
    elif containSpace:
        isValidVariable = False
        return isValidVariable
    elif otherChars:
        isValidVariable = False
        return isValidVariable
    return isValidVariable

name = "0ss"
result = variableName(name)
print(result)