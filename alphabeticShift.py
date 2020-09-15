# Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

def alphabeticShift(inputString):
    refList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    newList = []
    ouputString = ''
    for i in range(len(inputString)):
        char = inputString[i]
        if char == 'z':
            char = 'a'
            newList.append(char)
        else:
            refPosition = refList.index(char)+1
            char = refList[refPosition]
            newList.append(char)
    return (ouputString.join(newList))






inputString = "codesignal"
result = alphabeticShift(inputString)
print(result)