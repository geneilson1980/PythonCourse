import difflib

def stringsRearrangement(inputArray):
    expectectResult = False
    tempList = [inputArray]
    x = len(inputArray)
    i = 0
    count = 0
    while i < len(inputArray):
        a = inputArray[i]
        b = inputArray[i+1]
        c = a[0]
        for k in len(a):
            if a[k] != b[k]:
                count += 1


        # if i == len(inputArray)-1:
        #     i = 0
        # #     continue

        # j = 2
        # tempList[i].append(inputArray[j-1])
        i += 1



    return expectectResult


inputArray =["ab",  "ad",  "ef", "eg"]
result = stringsRearrangement(inputArray)
print(result)