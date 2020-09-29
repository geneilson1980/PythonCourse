def extractEachKth(inputArray, k):
    countK = 1
    newInputarray = []
    for i in range(len(inputArray)):
        test = inputArray[i]
        if countK == k:
            countK = 1
        else:
            newInputarray.append(inputArray[i])
            countK += 1
    return newInputarray

inputArray = [2, 4, 6, 8, 10]
k = 2
result = extractEachKth(inputArray, k)
print(result)