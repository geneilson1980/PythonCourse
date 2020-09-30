def arrayMaxConsecutiveSum(inputArray, k):
    newInput = inputArray.copy()
    expectedOutput = 0
    sumTemp = 0
    factor = 0
    for i in range(len(inputArray)):
        for j in range(k):
            x = newInput[j]
            sumTemp += newInput[j]
            factor += 1
            if sumTemp > expectedOutput and factor == k:
                expectedOutput = sumTemp            
        newInput.remove(newInput[0])
        sumTemp = 0
        factor = 0
        if len(newInput) < k:
            return expectedOutput


inputArray = [1, 3, 2, 4]
k = 3
result = arrayMaxConsecutiveSum(inputArray, k)
print(result)