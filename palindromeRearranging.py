# Given a string, find out if its characters can be rearranged to form a palindrome.

# Example

# For inputString = "aabb", the output should be
# palindromeRearranging(inputString) = true.

# We can rearrange "aabb" to make "abba", which is a palindrome.

def palindromeRearranging(inputString):
    distinctValues = list(set(inputString))
    isPalindrome = True
    stringSize = len(inputString)
    countOdd = 0
    if stringSize % 2 == 0:
        for i in range(len(distinctValues)):
            countChar = inputString.count(distinctValues[i])
            if countChar % 2 != 0:
                isPalindrome = False
                return isPalindrome
    else:
        for i in range(len(distinctValues)):
            countChar = inputString.count(distinctValues[i])
            if countChar % 2 != 0:
                countOdd += 1
                if countOdd > 1:
                    isPalindrome = False
                    return isPalindrome
    return isPalindrome

inputString = 'abbcabb'
result = palindromeRearranging(inputString)
print(result)


# I have used the following logic to solve this problem:

# 1. if string length is even then every character must have appeared even number of times.

# 2. else if string length is odd then only one character must have appeared odd number of times.