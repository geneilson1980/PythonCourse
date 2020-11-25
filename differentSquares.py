def differentSquares(matrix):
    expectedOutput = 0
    newList = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            tempElements = str(matrix[i][j]) + str(matrix[i][j+1]) + str(matrix[i+1][j]) + str(matrix[i+1][j+1])
            if tempElements not in newList:
                newList.append(tempElements)
    expectedOutput = len(newList)
    return expectedOutput

        
matrix = [[1,2,1], 
          [2,2,2], 
          [2,2,2], 
          [1,2,3], 
          [2,2,1]]

result = differentSquares(matrix)
print(result)