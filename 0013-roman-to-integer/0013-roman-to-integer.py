class Solution:
    def romanToInt(self, s: str) -> int:
        
        dictionary={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        
        if len(s)<2:
            return dictionary[s]
        left=0
        ans=0
        while left<len(s):
            if s[left:left+2] in dictionary:
                ans+=(dictionary[s[left:left+2]])
                left+=2
            elif s[left] in dictionary:
                ans+=(dictionary[s[left]])
                left+=1
        print(left)
        return ans
                
        