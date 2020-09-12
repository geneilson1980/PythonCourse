# Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

# Given two arrays a and b, check whether they are similar.

def areSimilar(a, b):
    similar = True
    countDif = 0
    c = []
    for j in range(len(a)):
        if a[j] != b[j]:
            countDif += 1
            c.append(j)
    for i in range(len(a)):
        if a[i] != b[i]:
            if a.count(a[i]) != b.count(a[i]):
                similar = False
                return similar
            elif countDif == 2:
                findNumber = b[c[1]]
                temp = b[c[0]]
                b[i] = findNumber
                b[c[1]] = temp
                if a != b:
                    similar = False
                    return similar
                else:
                    return similar
            else:
                similar = False
                return similar
    return similar


a = [2, 1, 2, 1, 1, 1, 2]
b = [1, 1, 2, 1, 2, 1, 2]
result = areSimilar(a, b)
print(result)