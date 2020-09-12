def isLucky(n):
    convertToString = str(n)
    totalDigits = int(len(convertToString) / 2)
    sumPart1 = 0
    sumPart2 = 0
    isLuck = False
    for i in range(0, totalDigits):
        sumPart1 += int(convertToString[i])
    for j in range(totalDigits, int(len(convertToString))):
        sumPart2 += int(convertToString[j])
    if sumPart1 == sumPart2:
        isLuck = True
    return isLuck

n = 239017
result = isLucky(n)
print(result)

