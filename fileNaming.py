def fileNaming(names):
    expectedOutput = []
    for value in names:
        if value not in expectedOutput:
            expectedOutput.append(value)
        else:
            sequentialNumber = expectedOutput.count(value)
            tempString = value + '(' + str(sequentialNumber) + ')'
            if tempString in expectedOutput:
                newSequentialNumber = expectedOutput.count(tempString) + 1
                newTempString = value + '(' + str(newSequentialNumber) + ')'
                expectedOutput.append(newTempString)
            else:
                expectedOutput.append(tempString)
    return expectedOutput



# names = ["doc", "doc", "image", "doc(1)", "doc"]
names = ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
result = fileNaming(names)
print(result)
