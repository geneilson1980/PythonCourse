def spiralNumbers(n):
    expectedOutput = n
    top = 0
    down = len(n)-1
    left = 0
    right = len(n)-1
    refNumber = 1
    dir = 0 # 0=Move left to right, 1=Move top to down, 2=Move right to left, 3=Move down to up
    while top <= down and left <= right:
        if dir == 0:
            for i in range(left, right+1):
                print(expectedOutput[top][i], end=' ')
            top += 1
            print('')
        elif dir == 1:
            for i in range(top, down+1):
                print(expectedOutput[i][right], end=' ')
            right -= 1
            print('')
        elif dir == 2:
            for i  in range(right, left-1, -1):
                print(expectedOutput[down][i], end=' ')
            down -= 1
            print('')
        elif dir == 3:
            for i  in range(down, top-1, -1):
                print(expectedOutput[i][left], end=' ')
            left += 1
        dir = (dir + 1) % 4
    return expectedOutput


# n = 3
n = [[1,2,3], [8,9,4], [7,6,5]]
result = spiralNumbers(n)
print(result)

#NEXT STEPS
# create new empty list
# populate the list
# populate last index with values.