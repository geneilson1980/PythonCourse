import difflib

def stringsRearrangement(inputArray):
    expectectResult = False
    tempList = [inputArray]
    x = len(inputArray)
    i = 0
    j = 0
    posI = 0
    count = 0
    while i < len(inputArray)-1:
        tempList.append([tempList[i][posI]])
        while j < len(inputArray)-2:
            temp = tempList[i][j+1]
            tempList[i+1].append(tempList[i][j+2])
            j += 1


    return expectectResult


inputArray =["ab",  "ad",  "ef", "eg"]
result = stringsRearrangement(inputArray)
print(result)