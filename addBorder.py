# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# Example

# For

# picture = ["abc",
#            "ded"]
# the output should be

# addBorder(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]

def addBorder(picture):
    longestString = 0
    resultList = []
    for string in picture:
        if len(string) > longestString:
            longestString = len(string)
    resultList.append(f'*'*(longestString+2))
    for string in picture:
        asterisk = '*'
        resultList.append(asterisk+string+asterisk)
    resultList.append(f'*'*(longestString+2))
    return resultList

a = ["abc","ded"]
result = addBorder(a)
print(result)