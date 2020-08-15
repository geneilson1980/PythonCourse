def adjacentElementsProduct(inputArray):
    count = len(inputArray)
    prod = 0
    largestprod = 0
    for i in range(0, count-1):
        prod = inputArray[i] * inputArray[i+1]
        if prod > largestprod:
            largestprod = prod
    return largestprod

array = [-23, 4, -3, 8, -12]
a = adjacentElementsProduct(array)
print(a)
