def arrayChange(inputArray):
    arraySize = len(inputArray) -1
    countMoves = 0
    for i in range(arraySize):
        currentValue = inputArray[i]
        nextValue = inputArray[i+1]
        if nextValue <= currentValue:
            difference = (currentValue - nextValue) + 1
            inputArray[i+1] = inputArray[i+1]  + difference
            countMoves += difference
    return countMoves

inputArray = [-1000, 0, -2, 0]
result = arrayChange(inputArray)
print(result)



