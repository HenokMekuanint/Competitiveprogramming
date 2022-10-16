class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        stack=[]
        for right in range(len(s)):
            while stack and s[right] in stack:
                stack.pop(0)
            stack.append(s[right])
            ans=max(ans,len(stack))
        return ans
