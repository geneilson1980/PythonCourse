def circleOfNumbers(n, firstNumber):
    expectedOutput = ''
    refDictionary = {4: 2, 6: 3, 8: 4, 10: 5, 12: 6, 14: 7, 16: 8, 18: 9, 20: 10}
    refNumber = refDictionary[n]
    if firstNumber + refNumber <= n:
        expectedOutput = firstNumber + refNumber
        return expectedOutput
    else:
        i = firstNumber
        count = 1
        while i <= n -1:
            if count == refNumber:
                expectedOutput = i
                return expectedOutput
            if i == n-1 and count != refNumber:
                i = 0
                continue
            count += 1
            i += 1

n = 10
firstNumber = 7
result = circleOfNumbers(n, firstNumber)
print(result)