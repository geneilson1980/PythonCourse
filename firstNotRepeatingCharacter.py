def firstNotRepeatingCharacter(s):
    countElems = {}
    for item in s:
        if item in countElems:
            countElems[item] += 1
        else:
            countElems[item] = 1
    for item in s:
        if countElems[item] == 1:
            return item
    return '_'

s = "ngrhhqbhnsipkcoqjyviikvxbxyphsnjpdxkhtadltsuxbfbrkof"
result = firstNotRepeatingCharacter(s)
print(result)