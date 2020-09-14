# Check if all digits of the given integer are even.
def evenDigitsOnly(n):
    convertNumToString = str(n)
    evenNumber = True
    for i in range(len(convertNumToString)):
        currentDigit = int(convertNumToString[i])
        if currentDigit % 2 != 0:
            evenNumber = False
            return evenNumber
    return evenNumber

n = 248622
result = evenDigitsOnly(n)
print(result)