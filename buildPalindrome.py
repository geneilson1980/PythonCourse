def buildPalindrome(st):
    while True:
        if st == st[::-1]:
            return st
        else:
            return st
    # return expectedOutput
    # APPROACH: get the string Base
    # after, get the next char and check is a palindr, if not get the next 2 chars toghter and reverted and so son

st = "aba"
result = buildPalindrome(st)
print(result)




# Just append the reverse of initial substrings of the string, from shortest to longest, to the string until you have a palindrome. e.g., for "acbab", try appending "a" which yields "acbaba", which is not a palindrome, then try appending "ac" reversed, yielding "acbabca" which is a palindrome.

# Update: Note that you don't have to actually do the append. You know that the substring matches since you just reversed it. So all you have to do is check whether the remainder of the string is a palindrome, and if so append the reverse of the substring. Which is what Ptival wrote symbolically, so he should probably get the credit for the answer. Example: for "acbab", find the longest suffix that is a palindrome; that is "bab". Then append the remainder, "ac", in reverse: ac bab ca.