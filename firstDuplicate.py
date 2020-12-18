def firstDuplicate(a):
    tempList = set()
    expectedOutput = 0
    if len(a) == len(set(a)):
        return -1
    else:
        for ele in a:
            if ele not in tempList:
                tempList.add(ele)
            else:
                expectedOutput = ele
                return expectedOutput

a = [2, 1, 3, 5, 4, 6]
result = firstDuplicate(a)
print(result)