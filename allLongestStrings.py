def allLongestStrings(inputArray):
    resultArray = []
    # longestStringNumber = len(inputArray[0])
    longestStringNumber = len(max(inputArray, key=len))
    # for string in inputArray:
    #     if len(string) > longestStringNumber:
    #         longestStringNumber = len(string)
    for string in inputArray:
        if len(string) == longestStringNumber:
            resultArray.append(string)
    return resultArray


# inputArray = ["aba", "aa", "ad", "vcd", "aba"]
inputArray = ["a","abc","cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]
resultArray = allLongestStrings(inputArray)
print(resultArray)