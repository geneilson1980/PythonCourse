def arrayMaxConsecutiveSum(inputArray, k):
    expectedOutput = 0
    sumTemp = 0
    factor = 1
    for i in range(len(inputArray)):
        if factor == k:
            if sumTemp > expectedOutput:
                expectedOutput = sumTemp 
                factor = 1
        else:
            sumTemp += inputArray[i]
            if i + k == len(inputArray):
                if sumTemp > expectedOutput:
                    expectedOutput = sumTemp
                return expectedOutput                
            else:
                factor += 1
    return expectedOutput

inputArray = [1, 3, 2, 4]
k = 3
result = arrayMaxConsecutiveSum(inputArray, 3)
print(result)