def sudoku(grid):
    expectedOutput = True
    tempList = []
    tempList2 = []
    count = 0
    refNumber = 0
    stopLooping = 0
    i = 0
    j = count
    countJ = 0
    for k in range(len(grid)):
        for l in range(len(grid)):
            if grid[k][l] not in tempList:
                bc = grid[k][l]
                tempList.append(grid[k][l])
            else:
                return False
            if grid[l][k] not in tempList2:
                tempList2.append(grid[l][k])
            else:
                return False
        tempList.clear()
        tempList2.clear()
    while i < len(grid):
        while j < len(grid):
            if grid[j] not in tempList:
                tempList.append(grid[i][j])
                j += 1
                countJ += 1
                if countJ == 3:
                    break
            else:
                return False
        refNumber += 1
        i += 1
        j = count
        countJ = 0
        if refNumber == 9:
            i = 0
            refNumber = 0
            count = j
            j = 3 + count
            count = j
            tempList.clear()
            stopLooping += 1
            if stopLooping == 3:
                break
        elif refNumber % 3 == 0:
            for element in tempList:
                if tempList.count(element) > 1:
                    return False
            tempList.clear()
            j = count
    return expectedOutput

grid = [[1,3,2,5,4,6,9,8,7], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4], 
 [9,2,1,4,3,5,8,7,6], 
 [3,5,4,7,6,8,2,1,9], 
 [6,8,7,1,9,2,5,4,3], 
 [5,7,6,9,8,1,4,3,2], 
 [2,4,3,6,5,7,1,9,8], 
 [8,1,9,3,2,4,7,6,5]]
result = sudoku(grid)
print(result)