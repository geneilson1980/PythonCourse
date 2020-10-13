def digitDegree(n):
    convertToString = str(n)
    sumTemp = 0
    countDDegree = 0
    if n < 10:
        return countDDegree
    else:
        countDDegree = 1
    while True:
        for i in range(len(convertToString)):
            sumTemp += int(convertToString[i])
        if sumTemp < 10:
            return countDDegree
        else:
            convertToString = str(sumTemp)
            countDDegree += 1
            sumTemp = 0
n = 877
result = digitDegree(n)
print(result)