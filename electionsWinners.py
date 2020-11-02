def electionsWinners(votes, k):
    votes.sort(reverse = True)
    expectedOutput = 0
    if votes[1] + k < votes[0]:
            expectedOutput += 1
            return expectedOutput
    for i in range(len(votes)):
        a = votes[0]
        if votes[i] + k > votes[0]:
            expectedOutput += 1
        else:
            return expectedOutput
    return expectedOutput

votes = [5, 1, 3, 4, 1]
k = 0
result = electionsWinners(votes, k)
print(result)