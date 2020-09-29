from itertools import permutations
import functools

def stringsRearrangement(inputArray):
    expectectResult = True
    newList = list(permutations(inputArray))
    x = len(newList)
    y = len(newList[0])
    # reduce = 0
    for i in range(len(newList)):
        for j in range(len(newList[0])-1):
            a = newList[i][j]
            b = newList[i][j+1]
            c = functools.reduce(lambda x, y: x + 1 if y[0] != y[1] else x, zip(a, b), 0)
            if c > 1:
                expectectResult = False
                break
        if c == 0 or c == 1:
            expectectResult = True
            return expectectResult
    return expectectResult

inputArray = ["abc", "abx", "axx", "abc"]
result = stringsRearrangement(inputArray)
print(result)