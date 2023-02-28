class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        p   w   w   k   e   w
        
        L
                R
        
        """
        ans=0
        dicti=defaultdict(int)
        left=0
        for right in range(len(s)):
            dicti[s[right]]+=1
            while sum(dicti.values())-len(dicti)>0:
                dicti[s[left]]-=1
                if dicti[s[left]]==0:
                    del dicti[s[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans