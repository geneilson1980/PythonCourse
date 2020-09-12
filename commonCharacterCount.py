def commonCharacterCount(s1, s2):
    sizeS1 = len(s1)
    sizeS2 = len(s2)
    NumCommonCha = 0
    dict1 = {}
    dict2 = {}
    for char in range(sizeS1):
        character = s1[char]
        countCharS1 = s1.count(s1[char])
        dict1[character] = countCharS1
    for char in range(sizeS2):
        character = s2[char]
        countCharS2 = s2.count(s2[char])
        dict2[character] = countCharS2
    for element in dict1:
        if element in dict2:
            if dict1[element] <= dict2[element]:
                NumCommonCha += dict1.get(element)
            else:
                NumCommonCha += dict2.get(element)
    return NumCommonCha

s1 = "abca"
s2 = "xyzbac"
result = commonCharacterCount(s1, s2)
print(result)