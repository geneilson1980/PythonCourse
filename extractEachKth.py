def extractEachKth(inputArray, k):
    newInputarray = []
    for i in range(1, len(inputArray)+1):
        if i % k != 0:
            newInputarray.append(inputArray[i-1])
    return newInputarray

inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
result = extractEachKth(inputArray, k)
print(result)