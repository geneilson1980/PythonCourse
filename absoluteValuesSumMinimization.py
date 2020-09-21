def absoluteValuesSumMinimization(a):
    smallestValue = 0
    sumAbs = pow(10, 10)
    sumTmp = 0
    for i in range(len(a)):
        for j in range(len(a)):
            sumTmp += abs(a[i] - a[j])
        if sumTmp < sumAbs:
            sumAbs = sumTmp
            smallestValue = a[i]
        sumTmp = 0
    return smallestValue

a = [2, 4, 7]
result = absoluteValuesSumMinimization(a)
print(result)