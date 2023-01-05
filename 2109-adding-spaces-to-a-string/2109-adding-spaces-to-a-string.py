class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=[]
        spaces=set(spaces)
        for i in range(len(s)):
            if i in spaces:
                ans.append(" ")
                ans.append(s[i])
            else:
                ans.append(s[i])
        return "".join(ans)
            
        