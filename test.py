# def adjacentElementsProduct(inputArray):
#     count = len(inputArray)
#     prod = 0
#     largestprod = None
#     for i in range(0, count-1):
#         prod = inputArray[i] * inputArray[i+1]
#         if largestprod == None:
#             largestprod = prod
#         if prod > largestprod:
#             largestprod = prod
#     return largestprod

# array = [-23, 4, -3, 8, -12]
# a = adjacentElementsProduct(array)
# print(a)



# def shapeArea(n):
#     a = n -1
#     previousPolygonArea = a**2
#     currentPolygonArea = n**2
#     polygonArea = previousPolygonArea + currentPolygonArea
#     return polygonArea

# polygon = shapeArea(100)
# print(polygon)



# def makeArrayConsecutive2(statues):
#     listSize = len(statues)
#     listSorted = sorted(statues)
#     test = []
#     count = 0
#     temp = listSorted[0] + 1
#     i = temp
#     while i < listSorted[-1]:
#         if temp not in listSorted:
#             test.append(temp)
#             count += 1
#         temp += 1
#         i+=1
#     return test
        
# statues = [6, 2, 3, 8]
# additionalStatues = makeArrayConsecutive2(statues)
# print(additionalStatues)


# def almostIncreasingSequence(sequence):
#     a = sequence[:-1]
#     b = sequence[1:]
#     for previous, next in zip(sequence[:-1], sequence[1:]):
#         if not previous < next:
#             return False
#     return True

# listSequence = [1, 3, 2, 1]
# a = almostIncreasingSequence(listSequence)
# print(a)

def almostIncreasingSequence(sequence):
    invalidItems = 0
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i-1]:
            invalidItems += 1
            if invalidItems > 1:
                return False
            if sequence[i] <= sequence[i-2] and sequence[i+1] <= sequence[i-1]:
                return False
    return True

sequence = [1, 3, 2, 1]
a = almostIncreasingSequence(sequence)
print(a) 