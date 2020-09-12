def avoidObstacles(inputArray):
    countJumps = 2
    i = 0
    refValue = len(inputArray)
    while i < refValue:
        num = inputArray[i]
        if num % countJumps == 0:
            countJumps += 1
            i = 0
        else:
            i += 1
    return countJumps

inputArray = [2, 3]
result = avoidObstacles(inputArray)
print(result)