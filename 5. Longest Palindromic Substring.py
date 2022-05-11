s = "babad"
def longestPalindrome(s):
    def IsPalindrome(s):
        if s == s[::-1]:
            return True
        else:
            return False
    if s == "":
        return s
    ansLen = 1
    ansStart = 0
    for i in range(1,len(s)):
        checkRange = i - ansLen
        if checkRange > 0 and IsPalindrome(s[checkRange-1:i+1]):
            ansLen += 2
            ansStart = checkRange-1
        elif checkRange >= 0 and  IsPalindrome(s[checkRange:i+1]):
            ansLen += 1
            ansStart = checkRange
    return s[ansStart:ansStart + ansLen]
print(longestPalindrome(s))
        
        