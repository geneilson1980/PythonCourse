# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

# def getResultStrig(inputString):
#     result = ''
#     while inputString.find('(') != -1:
#         findOpenBracket = inputString.rfind('(')
#         temp = inputString[findOpenBracket+1:]
#         temp2 = temp.find(')')+1
#         findCloseBracket = findOpenBracket + temp2
#         inputString = GetResultRevertedString(inputString, findOpenBracket, findCloseBracket)
#     result = inputString
#     return result

# def GetResultRevertedString(inputString, findOpenBracket, findCloseBracket):
#     substringBeforeBracket = inputString[0:findOpenBracket]
#     substringInBrackets = inputString[findOpenBracket+1:findCloseBracket]
#     substringAfterBracket = inputString[findCloseBracket+1:]
#     substringInBrackets = substringInBrackets[::-1]
#     inputString = substringBeforeBracket+substringInBrackets+substringAfterBracket
#     return inputString

# def reverseInParentheses(inputString):
#     stringSize = len(inputString)
#     countOpenBrackets = 0
#     countCloseBrackets = 0
#     for i in range(stringSize):
#         if inputString[i] == '(':
#             countOpenBrackets += 1
#         elif inputString[i] == ')':
#             countCloseBrackets += 1 
#     if inputString.find('(') == -1:
#         inputString = inputString[::-1]
#     else:
#         if countOpenBrackets > 1:
#             while inputString.find('(') != -1:
#                 inputString = getResultStrig(inputString)
#         else:
#             while inputString.find('(') != -1:
#                 findOpenBracket = inputString.find('(')
#                 findCloseBracket = inputString.find(')')
#                 inputString = GetResultRevertedString(inputString, findOpenBracket, findCloseBracket)
#     return inputString

def reverseInParentheses(s):
    while '(' in s:
        a = s.rfind('(')
        b = s.find(')', a)
        s = s[:a] + s[a+1:b][::-1] + s[b+1:]
    return s

inputString = "foo(bar(baz))blim"
result = reverseInParentheses(inputString)
print(result)

