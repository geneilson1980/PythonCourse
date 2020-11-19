def validTime(time):
    expectedOutput = True
    splitString = time.split(':')
    firstPart = int(splitString[0])
    secondPart = int(splitString[1])
    if firstPart >= 24 or secondPart >= 60:
        expectedOutput = False
    return expectedOutput

time = "13:58"
result = validTime(time)
print(result)