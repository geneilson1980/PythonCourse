from itertools import permutations
import functools
def stringsRearrangement(inputArray):
    expectectResult = False
    newList = list(permutations(inputArray))
    for i in range(len(newList)):
        for j in range(len(newList[0])-1):
            a = newList[i][j]
            b = newList[i][j+1]
            c = functools.reduce(lambda x, y: x + 1 if y[0] != y[1] else x, zip(a, b), 0)
            if c != 1:
                break
        if c == 1:
            expectectResult = True
            return expectectResult
    return expectectResult   

inputArray = ["abc", "abx", "axx", "abc"]
result = stringsRearrangement(inputArray)
print(result)


# Formula
# nPr = n!         4!       4.3.2.1     24     
#      ------  = -------- = -------- = ---- =  24 (24 different permutations )
#      (n-r)!      (4-3)!       1        1  

# ZIP function: Join two tuples together
# https://www.w3schools.com/python/ref_func_zip.asp

# Reduce Function: This function accepts a function and a sequence and returns a single value calculated 
# https://stackoverflow.com/questions/12226846/count-letter-differences-of-two-strings/40653556
# https://www.geeksforgeeks.org/reduce-in-python/

# Lambda Function: A lambda function is a small anonymous function. It can take any number of arguments, but can only have one expression.
# https://www.w3schools.com/python/python_lambda.asp