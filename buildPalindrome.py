def buildPalindrome(st):
    i = 1
    subString = st[:i]
    if st == st[::-1]:
        return st
    while True:
        revertSubstring = subString[::-1]
        sumString = st+revertSubstring
        if (st+revertSubstring) == sumString[::-1]:
            return st+revertSubstring
        else:
            i += 1
            subString = st[0:i]

st = "abcdc"
result = buildPalindrome(st)
print(result)