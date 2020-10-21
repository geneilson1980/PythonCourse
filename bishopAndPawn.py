def bishopAndPawn(bishop, pawn):
    expectedOutput = False
    refHash = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    value1 = refHash[bishop[0]] - refHash[pawn[0]] 
    value2 = int(bishop[1]) - int(pawn[1])
    if abs(value1) == abs(value2):
        expectedOutput = True
        return expectedOutput
    return expectedOutput

bishop = "e7"
pawn = "a3"
result = bishopAndPawn(bishop, pawn)
print(result)
