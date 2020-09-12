# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

def arrayMaximalAdjacentDifference(inputArray):
    maxDifference = 0
    for i in range(len(inputArray)-1):
        diff = inputArray[i] - inputArray[i+1]
        if abs(diff) > maxDifference:
            maxDifference = abs(diff)
    return maxDifference

inputArray = [-14, 15, -15]
result = arrayMaximalAdjacentDifference(inputArray)
print(result)