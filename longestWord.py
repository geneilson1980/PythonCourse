import re
def longestWord(text):
    refRegex = re.split('[^a-zA-Z]', text)
    expectedOutput = ''
    for word in refRegex:
        if not(word.isalpha()):
            continue
        else:
            if len(word) > len(expectedOutput):
                expectedOutput = word
    return expectedOutput

text = "Ready, steady, go!"
result = longestWord(text)
print(result)