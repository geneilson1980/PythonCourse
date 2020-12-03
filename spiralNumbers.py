def spiralNumbers(n):
    expectedOutput = []
    refNumber = 1
    for i in range(n):
        expectedOutput.append([])
        for j in range(refNumber, refNumber + n):
            expectedOutput[i].append(j)
            refNumber += 1


    return expectedOutput


n = 3
result = spiralNumbers(n)
print(result)