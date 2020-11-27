from functools import reduce
def digitsProduct(product):
    expectedOutput = ''
    inboundValue = product
    newList = []
    if inboundValue == 0:
        return 10
    elif product == 1:
        return 1
    else:
        for i in range(9, 1, -1):
            while inboundValue % i == 0: 
                newList.append(i)
                inboundValue = int(inboundValue / i)
            if i == 2 and len(newList) == 0:
                expectedOutput = -1
                return expectedOutput
        newList.sort()
        if reduce((lambda x, y: x * y ), newList) != product:
            return -1
        for value in newList:
            expectedOutput += str(value)
        return int(expectedOutput)

product = 596
result = digitsProduct(product)
print(result)