import re
def isMAC48Address(inputString):
    expectedOutput = True
    count = 1
    for i in range(len(inputString)):
        if count == 3:
            count = 1
            if inputString[i] != '-' or inputString[-1] == '-':
                expectedOutput = False
                return expectedOutput
        elif re.findall("[0-9A-F]", inputString[i]) == []:
            expectedOutput = False
            return expectedOutput
        else:
            count += 1
    return expectedOutput

inputString = "02-03-04-05-06-07-"
result = isMAC48Address(inputString)
print(result)