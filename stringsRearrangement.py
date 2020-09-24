def stringsRearrangement(inputArray):
    expectectResult = False
    tempList = inputArray
    for i in range(len(inputArray)-1):
        tempList.append(inputArray[i])
        for j in range(i+2, len(inputArray)+1):
            tempList.append(inputArray[j])
        tempList.append(inputArray[j-1])

    return expectectResult


inputArray =["ab",  "ad",  "ef", "eg"]
result = stringsRearrangement(inputArray)
print(result)