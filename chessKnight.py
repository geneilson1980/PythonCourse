def chessKnight(cell):
    refChar = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    expectedOutput = 0
    horizontalPos = refChar[cell[0]]
    verticalPos = 7 - (int(cell[1])-1)
    if ((verticalPos+1 >= 0) and (verticalPos+1 < 8)) and ((horizontalPos-2 >= 0) and (horizontalPos-2 < 8))  :
        expectedOutput += 1
    if ((verticalPos-1 >= 0) and (verticalPos-1 < 8)) and ((horizontalPos-2 >= 0) and (horizontalPos-2 <8))  :
        expectedOutput += 1
    if ((verticalPos-2 >= 0) and (verticalPos-2 < 8)) and ((horizontalPos-1 >= 0) and (horizontalPos-1 < 8))  :
        expectedOutput += 1
    if ((verticalPos-2 >= 0) and (verticalPos-2 < 8)) and ((horizontalPos+1 >= 0) and (horizontalPos+1 < 8))  :
        expectedOutput += 1
    if ((verticalPos-1 >= 0) and (verticalPos-1 < 8)) and ((horizontalPos+2 >= 0) and (horizontalPos+2< 8))  :
        expectedOutput += 1
    if ((verticalPos+1 >= 0) and (verticalPos+1 < 8)) and ((horizontalPos+2 >= 0) and (horizontalPos+2 < 8))  :
        expectedOutput += 1
    if ((verticalPos+2 >= 0) and (verticalPos+2 < 8)) and ((horizontalPos+1 >= 0) and (horizontalPos+1 < 8))  :
        expectedOutput += 1
    if ((verticalPos+2 >= 0) and (verticalPos+2 < 8)) and ((horizontalPos-1 >= 0) and (horizontalPos-1 < 8))  :
        expectedOutput += 1
    return expectedOutput

cell = "a3"
result = chessKnight(cell)
print(result)



# def chessKnight(cell):
#     chessBoard = [[1, 2, 3, 4, 5, 6, 7, 8,], [9, 10, 11, 12, 13, 14, 15, 16],
#                   [17, 18, 19, 20, 21, 22, 23, 24,], [25, 26, 27, 28, 29, 30, 31, 32],
#                   [33, 34, 35, 36, 37, 38, 39, 40,], [41, 42, 43, 44, 45, 46, 47, 48],
#                   [49, 50, 51, 52, 53, 54, 55, 56,], [57, 58, 59, 60, 61, 62, 63, 64]]
#     refChar = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
#     expectedOutput = 0
#     horizontalPos = refChar[cell[0]]
#     verticalPos = (len(chessBoard)-1) - (int(cell[1])-1)
#     if ((verticalPos+1 >= 0) and (verticalPos+1 < len(chessBoard))) and ((horizontalPos-2 >= 0) and (horizontalPos-2 < len(chessBoard)))  :
#         a = chessBoard[verticalPos+1][horizontalPos-2]
#         expectedOutput += 1
#     if ((verticalPos-1 >= 0) and (verticalPos-1 < len(chessBoard))) and ((horizontalPos-2 >= 0) and (horizontalPos-2 < len(chessBoard)))  :
#         b = chessBoard[verticalPos-1][horizontalPos-2]
#         expectedOutput += 1
#     if ((verticalPos-2 >= 0) and (verticalPos-2 < len(chessBoard))) and ((horizontalPos-1 >= 0) and (horizontalPos-1 < len(chessBoard)))  :
#         c = chessBoard[verticalPos-2][horizontalPos-1]
#         expectedOutput += 1
#     if ((verticalPos-2 >= 0) and (verticalPos-2 < len(chessBoard))) and ((horizontalPos+1 >= 0) and (horizontalPos+1 < len(chessBoard)))  :
#         d = chessBoard[verticalPos-2][horizontalPos+1]
#         expectedOutput += 1
#     if ((verticalPos-1 >= 0) and (verticalPos-1 < len(chessBoard))) and ((horizontalPos+2 >= 0) and (horizontalPos+2< len(chessBoard)))  :
#         e = chessBoard[verticalPos-1][horizontalPos+2]
#         expectedOutput += 1
#     if ((verticalPos+1 >= 0) and (verticalPos+1 < len(chessBoard))) and ((horizontalPos+2 >= 0) and (horizontalPos+2 < len(chessBoard)))  :
#         f = chessBoard[verticalPos+1][horizontalPos+2]
#         expectedOutput += 1
#     if ((verticalPos+2 >= 0) and (verticalPos+2 < len(chessBoard))) and ((horizontalPos+1 >= 0) and (horizontalPos+1 < len(chessBoard)))  :
#         g = chessBoard[verticalPos+2][horizontalPos+1]
#         expectedOutput += 1
#     if ((verticalPos+2 >= 0) and (verticalPos+2 < len(chessBoard))) and ((horizontalPos-1 >= 0) and (horizontalPos-1 < len(chessBoard)))  :
#         h = chessBoard[verticalPos+2][verticalPos-1]
#         expectedOutput += 1
#     return expectedOutput