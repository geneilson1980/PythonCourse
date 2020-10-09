def growingPlant(upSpeed, downSpeed, desiredHeight):
    expectedOutput = 1
    resultTemp = upSpeed
    while resultTemp < desiredHeight:
        resultTemp += upSpeed - downSpeed
        expectedOutput += 1
    return expectedOutput 

upSpeed = 10
downSpeed = 9
desiredHeight = 4
result = growingPlant(upSpeed, downSpeed, desiredHeight)
print(result)