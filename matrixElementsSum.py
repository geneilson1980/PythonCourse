# def matrixElementsSum(matrix):
#     sum = 0
#     ref = ''
#     for i in range(0, len(matrix)):
#         k = len(matrix[i])
#         for j in range(0, k):
#             if matrix[i][j] == 0:
#                 ref = j
#                 a = i
#             if ref != '':
#                 while a < len(matrix):
#                     matrix[a][ref] = 0
#                     a+=1
#                 ref = ''
#         for j in range(0, k):
#             if matrix [i][j] != 0:
#                 sum += matrix [i][j]   
#     return sum

def matrixElementsSum(matrix):
    sum = 0
    hauntedIndex = []
    # a = len(matrix)
    for i in range(len(matrix)):
        # b = len(matrix[i])
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                hauntedIndex.append(j)
                test = hauntedIndex.index(j)
            elif hauntedIndex.index(j) != test:
                sum += matrix [i][j]   
    return sum


matrix = [[0, 1, 1, 2], 
          [1, 5, 0, 0], 
          [2, 0, 3, 3]]


res = matrixElementsSum(matrix)
print(res)

