def spiralNumbers(n):
    newList = [[]* n for i in range(n)]
    top = 0
    down = n-1
    left = 0
    right = n-1
    refNumber = 1
    dir = 0 # 0=Move left to right, 1=Move top to down, 2=Move right to left, 3=Move down to up
    while top <= down and left <= right:
        if dir == 0: #This if will populate the top line (horizontal)
            for i in range(left, right+1):
                newList[top].insert(i, refNumber)
                refNumber += 1
            top += 1
        elif dir == 1: #This elif will populate the last empty column (vertical)
            for i in range(top, down+1):
                newList[i].insert(left, refNumber)
                refNumber += 1
            right -= 1
        elif dir == 2: #This elif will populate the bottom line (horizontal)
            for i  in range(right, left-1, -1):
                newList[down].insert(left, refNumber)
                refNumber += 1
            down -= 1
        elif dir == 3: #This elif will populate the first column (vertical, down to top)
            for i  in range(down, top-1, -1):
                newList[i].insert(left, refNumber)
                refNumber += 1
            left += 1
        dir = (dir + 1) % 4
    return newList


n = 5
result = spiralNumbers(n)
print(result)