def GetFactorial(n):
    #base case
    if n == 0 or n == 1:
        return 1
    return n * GetFactorial(n -1)

print(GetFactorial(5))