def arrayMaxConsecutiveSum(inputArray, k):
    expectedOutput = 0
    sumTemp = 0
    listSize = len(inputArray)
    for i in range(k):
        sumTemp += inputArray[i]
    expectedOutput = sumTemp
    for j in range(1, len(inputArray)-1):
        sumTemp = sumTemp - inputArray[j-1]
        x = inputArray[j+(k-1)]
        sumTemp = sumTemp + inputArray[j+(k-1)]
        if sumTemp > expectedOutput:
            expectedOutput = sumTemp
        z = (j + (k-1)) 
        w = len(inputArray)-1
        if (j + (k-1)) >= len(inputArray)-1:
            return expectedOutput
    return expectedOutput

inputArray = [3, 2, 1, 1]
k = 1
result = arrayMaxConsecutiveSum(inputArray, k)
print(result)

# Free hint: imagine if your k = 1000, and length of array = 10000.
# every new cycle you need to compute sum of 1000 elements.
# but the difference between previous sum and current sum is just two components.
# so, think how you can avoid naive summation of 1000 components