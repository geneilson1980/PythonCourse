def longestDigitsPrefix(inputString):
    expectedOutput = ''
    for i in range(len(inputString)):
        currentValue = inputString[i]
        if not(currentValue.isnumeric()):
            return expectedOutput
        else:
            expectedOutput += currentValue
    return expectedOutput

inputString = "aaaaaaa"
result = longestDigitsPrefix(inputString)
print(result)