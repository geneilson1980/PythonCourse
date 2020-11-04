def lineEncoding(s):
    expectedOutput = ''
    uniqueChar = []
    countChar = 1
    i = 0
    while i < len(s):
        if s[i] == s[i+1]:
            countChar += 1
            i += 1
            if i == len(s)-1:
                expectedOutput = expectedOutput + str(countChar) + s[i]
            continue
        else:
            if countChar == 1:
                expectedOutput = expectedOutput + s[i]
                if i == len(s)-1:
                    expectedOutput = expectedOutput + s[i+1]
            else:
                expectedOutput = expectedOutput + str(countChar) + s[i]
            countChar = 1
            i += 1
    return expectedOutput

s = "aabbbc"
result = lineEncoding(s)
print(result)