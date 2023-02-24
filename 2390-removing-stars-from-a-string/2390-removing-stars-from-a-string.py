class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]!="*":
                stack.append(s[i])
            elif stack:
                stack.pop(-1)
        return "".join(stack)
                