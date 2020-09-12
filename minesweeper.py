# In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

def minesweeper(matrix):
    matrixRowSize = len(matrix)
    matrixColSize = len(matrix[0])
    newMatrix = [[]]
    tempList = []
    countValues = 0
    for i in range(matrixRowSize):
        for j in range(matrixColSize):
            #Start position
            if i == 0 and j == 0:
                upValue = False
                upBackValue = False
                backValue = False
                downBackValue = False
                downValue = matrix[i+1][j]
                downFrontValue = matrix[i+1][j+1]
                frontValue = matrix[i][j+1]
                upFrontValue = False
            #Line 0 and run through j (in the middle of list)
            elif i == 0 and j > 0 and j < matrixColSize-1:
                upValue = False
                upBackValue = False
                backValue = matrix[i][j-1]
                downBackValue = matrix[i+1][j-1]
                downValue = matrix[i+1][j]
                downFrontValue = matrix[i+1][j+1]
                frontValue = matrix[i][j+1]
                upFrontValue = False
            #Line 0 and get the last j value
            elif i == 0 and j > 0 and j == matrixColSize -1:
                upValue = False
                upBackValue = False
                backValue = matrix[i][j-1]
                downBackValue = matrix[i+1][j-1]
                downValue = matrix[i+1][j]
                downFrontValue = False
                frontValue = False
                upFrontValue = False
            #Middle of list, j at position 0
            elif i > 0 and i != matrixRowSize-1 and i < matrixRowSize and j == 0 and j < matrixColSize-1:
                upValue = matrix[i-1][j]
                upBackValue = False
                backValue = False
                downBackValue = False
                downValue = matrix[i+1][j]
                downFrontValue = matrix[i+1][j+1]
                frontValue = matrix[i][j+1]
                upFrontValue = matrix[i-1][j+1]
            #Middle list
            elif i > 0 and i != matrixRowSize-1 and j > 0 and j < matrixColSize -1:
                upValue = matrix[i-1][j]
                upBackValue = matrix[i-1][j-1]
                backValue = matrix[i][j-1]
                downBackValue = matrix[i+1][j-1]
                downValue = matrix[i+1][j]
                downFrontValue = matrix[i+1][j+1]
                frontValue = matrix[i][j+1]
                upFrontValue = matrix[i-1][j+1]
            #Middle list, last j position
            elif i > 0 and i != matrixRowSize-1 and j > 0 and j == matrixColSize -1:
                upValue = matrix[i-1][j]
                upBackValue = matrix[i-1][j-1]
                backValue = matrix[i][j-1]
                downBackValue = matrix[i+1][j-1]
                downValue = matrix[i+1][j]
                downFrontValue = False
                frontValue = False
                upFrontValue = False
            #Last line, j at position 0
            elif i == matrixRowSize-1 and j == 0:
                upValue = matrix[i-1][j]
                upBackValue = False
                backValue = False
                downBackValue = False
                downValue = False
                downFrontValue = False
                frontValue = matrix[i][j+1]
                upFrontValue = matrix[i-1][j+1]
            #Last line, j > 0 (middle of the list)
            elif i == matrixRowSize-1 and j > 0 and j < matrixColSize -1:
                upValue = matrix[i-1][j]
                upBackValue = matrix[i-1][j-1]
                backValue = matrix[i][j-1]
                downBackValue = False
                downValue = False
                downFrontValue = False
                frontValue = matrix[i][j+1]
                upFrontValue = matrix[i-1][j+1]
            #Last line, j at last position
            else:
                upValue = matrix[i-1][j]
                upBackValue = matrix[i-1][j-1]
                backValue = matrix[i][j-1]
                downBackValue = False
                downValue = False
                downFrontValue = False
                frontValue = False
                upFrontValue = False
            # else:
            #     upValue = matrix[i-1][j]
            #     upBackValue = matrix[i-1][j-1]
            #     backValue = matrix[i][j-1]
            #     downBackValue = matrix[i+1][j-1]
            #     downValue = matrix[i+1][j]
            #     downFrontValue = matrix[i+1][j+1]
            #     frontValue = matrix[i][j+1]
            #     upFrontValue = matrix[i-1][j+1]
            tempList.append(upBackValue)
            tempList.append(backValue)
            tempList.append(downBackValue)
            tempList.append(downValue)
            tempList.append(downFrontValue)  
            tempList.append(frontValue)          
            tempList.append(upFrontValue)            
            tempList.append(upValue)
            countValues = tempList.count(True)
            newMatrix[i].append(countValues)
            tempList.clear()
            countValues = 0
        if i != matrixRowSize - 1:
            # return newMatrix
            newMatrix.append([])
    return newMatrix

matrix = [[True,False,False], 
 [False,True,False], 
 [False,False,False]]

result = minesweeper(matrix)
print(result)
