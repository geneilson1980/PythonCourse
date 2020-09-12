def sortByHeight(a):
    tempList = []
    for height in a:
        if height != -1:
            tempList.append(height)
    tempList.sort()
    j = 0
    test = len(a)
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = tempList[j]
            j += 1
    return a


# def sortByHeight(a):
#     for i in range(len(a), 0, -1):
#         for j in range(0, i-1):
#             test1 = a[j]
#             test2 = a[j+1]
#             if a[j] != -1:
#                 if a[j+1] != -1:                    
#                     if a[j] > a[j+1]:
#                         x = a[j]
#                         a[j] = a[j+1]
#                         a[j+1] = x
#                 else:
#                     k = j
#                     while a[k+1] == -1:
#                         k = k + 1
#                     test3 = a[k+1]
#                     if a[j] > a[k+1]:
#                         x = a[j]
#                         a[j] = a[k+1]
#                         a[k+1] = x
#     return a

a = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
result = sortByHeight(a)
print(result)