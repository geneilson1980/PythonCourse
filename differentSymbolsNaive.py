def differentSymbolsNaive(s):
    newString = []
    for i in range(len(s)):
        if s[i] not in newString:
            newString.append(s[i])
    countDiffSymbols = len(newString)
    return countDiffSymbols



s = "cabca"
result = differentSymbolsNaive(s)
print(result)