def fileNaming(names):
    expectedOutput = []
    sequentialNumber = 1
    for value in names:
        sequentialNumber = names.count(value)
        if value in expectedOutput:
            continue
        elif sequentialNumber == 1:
            expectedOutput.append(value)
<<<<<<< Updated upstream
        else:
            while True:
                tempString = value + '(' + str(sequentialNumber) + ')'
                if tempString not in expectedOutput:
                    expectedOutput.append(tempString)
                    sequentialNumber = 1
                    break
                else:
                    sequentialNumber += 1
=======
        elif sequentialNumber > 1:
            expectedOutput.append(value)
            for i in range(1, sequentialNumber):
                expectedOutput.append(value + '(' + str(i) + ')')
>>>>>>> Stashed changes
    return expectedOutput



names = ["doc", "doc", "image", "doc(1)", "doc"]
# names = []
result = fileNaming(names)
print(result)
