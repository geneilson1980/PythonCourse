def lineEncoding(s):
    expectedOutput = ''
    countChar = 1
    x = len(s)
    for i in range(len(s)):
        if i == len(s)-1:
            if s[i] != s[i-1]:
                expectedOutput = expectedOutput + s[i]
            else:
                expectedOutput = expectedOutput + str(countChar) + s[i]
        elif s[i] == s[i+1]:
            countChar += 1
        elif s[i] != s[i+1]:
            if countChar == 1:
                expectedOutput = expectedOutput + s[i]
            else:
                expectedOutput = expectedOutput + str(countChar) + s[i]
            countChar = 1
        else:
            expectedOutput = expectedOutput + str(countChar) + s[i+1]
            return expectedOutput
    return expectedOutput

s = "bbjaadlkjdl"
result = lineEncoding(s)
print(result)