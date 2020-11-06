def chessKnight(cell):
    chessBoard = [[1, 0, 1, 0, 1, 0, 1, 0,], [0, 1, 0, 1, 0, 1, 0, 1], 
                  [1, 0, 1, 0, 1, 0, 1, 0,], [0, 1, 0, 1, 0, 1, 0, 1], 
                  [1, 0, 1, 0, 1, 0, 1, 0,], [0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0,], [0, 1, 0, 1, 0, 1, 0, 1]]
    refChar = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    expectedOutput = 0
    pos1 = cell[0]
    pos1a = int(cell[1])
    getPos = refChar[pos1]
    valueInChessBoard = chessBoard[getPos][pos1a-1]
    if valueInChessBoard is True:
        print('hello')
    else:
        print('no hello')
    

    return expectedOutput



cell = "A1"
result = chessKnight(cell)
print(result)