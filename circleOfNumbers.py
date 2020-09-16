def circleOfNumbers(n, firstNumber):
    expectedOutput = ''
    refDictionary = {4: 2, 6: 3, 8: 4, 10: 5, 12: 6, 14: 7, 16: 8, 18: 9, 20: 10}
    refNumber = refDictionary[n]
    expectedOutput = refNumber + firstNumber
    return expectedOutput

    #I have to develop the another part of the code, where the number should continue restarting from 0

n = 18
firstNumber = 5
result = circleOfNumbers(n, firstNumber)
print(result)