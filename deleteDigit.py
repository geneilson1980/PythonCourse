def deleteDigit(n):
    maximalNumber = 0
    convertNumToString = str(n)
    for i in range(len(convertNumToString)):
        temporaryNumber = int(convertNumToString[:i] + convertNumToString[i+1:])
        if temporaryNumber > maximalNumber:
            maximalNumber = temporaryNumber
    return maximalNumber

n = 861452
result = deleteDigit(n)
print(result)