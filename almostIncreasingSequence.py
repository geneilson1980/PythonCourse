def almostIncreasingSequence(sequence):
    preNum = -99999999
    for i in range(len(sequence)):
        num = sequence[i]
        if not num  > preNum:
            index = i
            a = sequence[:index]
            b = sequence[index + 1:]
            c = sequence[:index + 1]
            d = sequence[index + 1 + 1:]
            e = sequence[:index - 1]
            f = sequence[index + 1 - 1:]
            seq1 = sequence[:index] + sequence[index + 1:]
            seq2 = sequence[:index + 1] + sequence[index + 1 + 1:]
            seq3 = sequence[:index - 1] + sequence[index + 1 - 1:]
            g = isIncreaseSequence(seq1)
            h = isIncreaseSequence(seq2)
            j = isIncreaseSequence(seq3)
            if isIncreaseSequence(seq1) or isIncreaseSequence(seq2) or isIncreaseSequence(seq3):
                return True
        preNum = num
    return False

def isIncreaseSequence(sequence):
    preNum = -99999999
    for num in sequence:
        if not num > preNum:
            return False
        preNum = num
    return True

test = [1, 3, 2, 1]
resultado = almostIncreasingSequence(test)
print(resultado)