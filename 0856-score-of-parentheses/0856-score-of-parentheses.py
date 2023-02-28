class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        import math
        ans=0
        bal=0
        for  i in range(len(s)):
            if s[i]=="(":
                bal+=1
            else:
                bal-=1
                if s[i-1]=="(":
                    ans=ans+math.pow(2,bal)
        return int(ans)