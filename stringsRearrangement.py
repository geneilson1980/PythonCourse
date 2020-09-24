def stringsRearrangement(inputArray):
    expectectResult = False
    tempList = [[inputArray]]
    x = len(inputArray)
    for i in range(1, len(inputArray)-1):
        tempList.append([inputArray[i-1]])
        for j in range(i+2, len(inputArray)+1):
            tempList.append([[inputArray[i-1]]][inputArray[j-1]])
        tempList.append(inputArray[i])


    return expectectResult


inputArray =["ab",  "ad",  "ef", "eg"]
result = stringsRearrangement(inputArray)
print(result)