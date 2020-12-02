def fileNaming(names):
    expectedOutput = []
    sequentialNumber = 1
    for value in names:
        if value not in expectedOutput:
            expectedOutput.append(value)
        else:
            while True:
                tempString = value + '(' + str(sequentialNumber) + ')'
                if tempString not in expectedOutput:
                    expectedOutput.append(tempString)
                    sequentialNumber = 1
                    break
                else:
                    sequentialNumber += 1
    return expectedOutput



names = ["doc", "doc", "image", "doc(1)", "doc"]
# names = []
result = fileNaming(names)
print(result)
