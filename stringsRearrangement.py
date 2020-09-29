from itertools import permutations
import functools
def stringsRearrangement(inputArray):
    expectectResult = False
    newList = list(permutations(inputArray))
    for i in range(len(newList)):
        for j in range(len(newList[0])-1):
            a = newList[i][j]
            b = newList[i][j+1]
            c = functools.reduce(lambda x, y: x + 1 if y[0] != y[1] else x, zip(a, b), 0)
            if c != 1:
                break
        if c == 1:
            expectectResult = True
            return expectectResult
    return expectectResult   

inputArray = ["abc", "abx", "axx", "abc"]
result = stringsRearrangement(inputArray)
print(result)