def circleOfNumbers(n, firstNumber):
    expectedOutput = ''
    refDictionary = {4: 2, 6: 3, 8: 4, 10: 5, 12: 6, 14: 7, 16: 8, 18: 9, 20: 10}
    refList = []
    for i in range(n):
        refList.append(i)
    refNumber = refDictionary[n]
    refIndexFNumber = refList.index(firstNumber)
    i = firstNumber
    cicle = 0
    count = 1
    while True:
        if count == refNumber:
            expectedOutput = i
            return expectedOutput
        if i == n-1 and count != refNumber:
            i = 0
            count += 1
            continue
        count += 1
        i += 1


    #I have to develop the another part of the code, where the number should continue restarting from 0

n = 6
firstNumber = 3
result = circleOfNumbers(n, firstNumber)
print(result)



# This test case will be hidden from candidates.
# Input:
# n: 4
# firstNumber: 3
# Output:
# null
# Expected Output:
# 1

    # while i  < n:
    #     if count == refNumber:
    #         if cicle == 0:
    #             expectedOutput = i + 1
    #             return expectedOutput
    #         else:
    #             expectedOutput = i
    #             return expectedOutput
    #     if i == n-1 and count != refNumber:
    #         i = 0
    #         cicle += 1 
    #         continue
    #     count += 1
    #     i += 1