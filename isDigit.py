def isDigit(symbol):
    if symbol.isnumeric():
        expectedOutput = True
        return expectedOutput
    else:
        expectedOutput = False
        return expectedOutput

symbol = 'O'
result = isDigit(symbol)
print(result)
