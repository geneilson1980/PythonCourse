# Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.^
import re
def variableName(name):
    isValidVariable = True
    containNumbers = re.findall('[0-9]', name[0])
    containLetters = re.findall('[a-zA-Z]', name[0])
    containUnderscore = re.findall('_', name)
    containTrace = re.findall('-', name)
    containSpace = re.findall(' ', name)
    otherChars = re.findall('^[a-zA-Z][0-9]', name)
    if not(containLetters) or not(containUnderscore):
        isValidVariable = False
        return isValidVariable
    elif containSpace:
        isValidVariable = False
        return isValidVariable
    

    return isValidVariable

name = "va[riable0"
result = variableName(name)
print(result)