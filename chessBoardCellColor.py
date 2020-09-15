def chessBoardCellColor(cell1, cell2):
    chessBoard = [[1, 0, 1, 0, 1, 0, 1, 0,], [0, 1, 0, 1, 0, 1, 0, 1], 
                  [1, 0, 1, 0, 1, 0, 1, 0,], [0, 1, 0, 1, 0, 1, 0, 1], 
                  [1, 0, 1, 0, 1, 0, 1, 0,], [0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0,], [0, 1, 0, 1, 0, 1, 0, 1]]
    refChar = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    resultOutput = True
    pos1 = cell1[0]
    pos1a = int(cell1[1])
    pos2 = cell2[0]
    pos2a = int(cell2[1])
    getPos1 = refChar[pos1] 
    getPos2 = refChar[pos2]
    value1InChessBoard = chessBoard[getPos1][pos1a-1]
    value2InChessBoard = chessBoard[getPos2][pos2a-1]
    if value1InChessBoard != value2InChessBoard:
        resultOutput = False
        return resultOutput
    return resultOutput

cell1 = "A1"
cell2 = "B2"
result = chessBoardCellColor(cell1, cell2)
print(result)
