# Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        x = inputArray[i]
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem
    return inputArray

inputArray = [10, 10]
elemToReplace =  0
substitutionElem = 9
result = arrayReplace(inputArray, elemToReplace, substitutionElem)
print(result)