def longestDigitsPrefix(inputString):
    tempString = ''
    expectedOutput = ''
    for i in range(len(inputString)):
        a = inputString.find(' ')
        if inputString.find(' ') != -1:
            return expectedOutput
        currentValue = inputString[i]
        if currentValue.isnumeric():
            tempString += currentValue
            if len(tempString) > len(expectedOutput):
                expectedOutput = tempString
        else:
            tempString = ''
    return expectedOutput

inputString = "always"
result = longestDigitsPrefix(inputString)
print(result)