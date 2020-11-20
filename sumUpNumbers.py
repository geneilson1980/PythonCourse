import re
def sumUpNumbers(inputString):
    sumOfNumbers = 0
    newList = re.split("[^0-9]", inputString)
    for value in newList:
        if value.isdigit():
            sumOfNumbers += int(value)
    return sumOfNumbers
    
inputString = "123450"
result = sumUpNumbers(inputString)
print(result)