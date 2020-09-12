def alternatingSums(a):
    listSize = len(a)
    alternatingSums = []
    sumTeam1 = 0
    sumTeam2 = 0
    for i in range(listSize):
        if i % 2 != 0:
            sumTeam1 += a[i]
        else:
            sumTeam2 += a[i]
    
    alternatingSums.append(sumTeam1)
    alternatingSums.append(sumTeam2)
    return alternatingSums

a = [80, 0]
result = alternatingSums(a)
print(result)