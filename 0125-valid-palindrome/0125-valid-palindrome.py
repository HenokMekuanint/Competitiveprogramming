class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        
        temp=""
        
        for alp in s:
            if alp.isalpha() or  alp.isdigit():
                temp+=alp
        return temp==temp[::-1]
        