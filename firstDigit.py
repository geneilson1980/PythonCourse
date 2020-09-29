def firstDigit(inputString):
    for i, e in enumerate(inputString):
        if e.isnumeric():
            return e

inputString = "_Aas_23"
result = firstDigit(inputString)
print(result)