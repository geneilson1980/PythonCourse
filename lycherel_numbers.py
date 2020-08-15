# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

# Not all numbers produce palindromes so quickly. For example,

# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337

# That is, 349 took three iterations to arrive at a palindrome.

# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

# How many Lychrel numbers are there below ten-thousand?

# NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

def GetPalindrome(number):
    isPalindrome = False
    a = number
    sum = 0
    for i in range(1, 50):
        b = int(str(a)[::-1])
        sum = a + b
        c = int(str(sum)[::-1])
        if sum == c:
            isPalindrome = True
            break
        else:
            a = sum
    return isPalindrome

target = 10000
lychrelNumbers = []
count = 0

for i in range(10, target):
    value = GetPalindrome(i)
    if not(value):
        # lychrelNumbers.append(i)
        count += 1

# lychrelCount = len(lychrelNumbers)
# print(f'There are {lychrelCount} Lychrel numbers below ten-thousand')
print(f'There are {count} Lychrel numbers below ten-thousand')