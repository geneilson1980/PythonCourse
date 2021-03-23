import math
def rotateImage(a):
    listSize = len(a)
    for i in range(listSize):
        for j in range(i, listSize):
            temp = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = temp
    
    for i in range(listSize):
        for j in range(int(math.floor(listSize/2))):
            temp = a[i][j]
            a[i][j] = a[i][listSize-1-j]
            a[i][listSize-1-j] = temp
    return a

a = [[1,2,3], [4,5,6], [7,8,9]]
result = rotateImage(a)
print(result)