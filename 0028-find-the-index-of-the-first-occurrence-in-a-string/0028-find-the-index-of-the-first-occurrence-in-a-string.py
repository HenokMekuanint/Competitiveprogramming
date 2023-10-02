class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                
                if i+len(needle)<len(haystack)+1 and  haystack[i:i+len(needle)]==needle:
                    return i
        return -1
        