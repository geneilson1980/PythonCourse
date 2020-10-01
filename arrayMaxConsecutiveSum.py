def arrayMaxConsecutiveSum(inputArray, k):
    newInput = inputArray.copy()
    expectedOutput = 0
    sumTemp = 0
    factor = 0
    refValue = 0
    listSize = len(inputArray)
    for i in range(listSize):
        resultSum = sumValues(i, k, inputArray)
        if resultSum <= refValue:
            if i + k >= listSize:
                return expectedOutput
            else:
                continue
        else:
            refValue = resultSum
        if i + k >= listSize:
            if resultSum > expectedOutput:
                expectedOutput = resultSum    
                return expectedOutput
            else:
                return expectedOutput
        elif resultSum > expectedOutput:
            expectedOutput = resultSum

def sumValues(position, factor, list):
    sumValuesList = 0
    listSize = len(list)
    countFactor = 0
    for i in range(position, listSize):
        sumValuesList += list[i]
        countFactor += 1
        if countFactor == factor:
            return sumValuesList



inputArray = [2, 3, 5, 1, 6]
k = 2
result = arrayMaxConsecutiveSum(inputArray, k)
print(result)


# def fib_rapido(n):
#     if n == 1 or n == 2:
#         return 1
#     f1 = 1
#     f2 = 1
#     for i in range(3, n + 1):
#         f = f1 + f2
#         f2 = f1
#         f1 = f
#     return f1

# print(fib_rapido(7))




# def arrayMaxConsecutiveSum(inputArray, k):
#     newInput = inputArray.copy()
#     expectedOutput = 0
#     sumTemp = 0
#     factor = 0
#     for i in range(len(inputArray)):
#         for j in range(k):
#             x = newInput[j]
#             sumTemp += newInput[j]
#             factor += 1
#             if sumTemp > expectedOutput and factor == k:
#                 expectedOutput = sumTemp            
#         newInput.remove(newInput[0])
#         sumTemp = 0
#         factor = 0
#         if len(newInput) < k:
#             return expectedOutput


inputArray = [1, 3, 2, 4]
k = 3
result = arrayMaxConsecutiveSum(inputArray, k)
print(result)