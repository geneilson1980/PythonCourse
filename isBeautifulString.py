def isBeautifulString(inputString):
    expectedOutput = True
    alphabet = {'0' : 'a', '1' : 'b', '2' : 'c', '3' : 'd', '4' : 'e', '5' : 'f', '6' : 'g', '7' : 'h', '8' : 'i', '9' : 'j', '10' : 'k', '11' : 'l', '12' : 'm', '13' : 'n', '14' : 'o', '15' : 'p', '16' : 'q', '17' : 'r', '18' : 's', '19' : 't', '20' : 'u', '21' : 'v', '22' : 'w', '23' : 'x', '24' : 'y', '25' : 'z'}
    uniqueValues = []
    for char in inputString:
        if char not in uniqueValues:
            uniqueValues.append(char)
    for i in range(len(uniqueValues)):
        string1 = uniqueValues[i]
        string2 = alphabet[i+1]
        countVaule1 = inputString.count(string1)
        countVaule2 = inputString.count(string2)
        if countVaule1 != countVaule2:
            expectedOutput = False
            return expectedOutput
    return expectedOutput

inputString = "bbbaacdafe"
result = isBeautifulString(inputString)
print(result)

# identify the letter in alphabet to fill out the string2 variable, after,I have to compare it normally.