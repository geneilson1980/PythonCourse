def bishopAndPawn(bishop, pawn):
    expectedOutput = False
    # chestBoard = []
    refHash = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    refBishop = refHash[bishop[0]] 
    refPawn = refHash[pawn[0]]
    chestBoard = [[0]*8]*8
    a = refHash[bishop[0]]
    b = int(bishop[1])
    # chestBoard[refHash[bishop[0]]][refHash[bishop[1-1]]] = bishop[1]
    chestBoard[0][0] = 1



    # for i in range(8):
    #     column = []
    #     for j in range(8):
    #         column.append(0)
    #     chestBoard.append(column)
    return expectedOutput

bishop = "a1"
pawn = "c3"
result = bishopAndPawn(bishop, pawn)
print(result)


# Creating a hash map to relate the bishop and pawn values to includ it in the chest board.


# cinema =[
#     [ 0, 0, 0, 0, 1 ],
#     [ 0, 0, 0, 1, 1 ],
#     [ 0, 0, 1, 1, 1 ],
#     [ 0, 0, 0, 1, 1 ],
#     [ 0, 0, 0, 0, 1 ]
# ]

# cinema[1][0] = 1
# print(cinema)