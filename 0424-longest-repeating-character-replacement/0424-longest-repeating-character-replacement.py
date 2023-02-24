class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        "   A   B   A   B   "
        
            L
            
                R
            dicti={
            "A":1,
            "B":1,
            
            
            }
        
        """
        dicti=defaultdict(int)
        left=0
        ans=float("-inf")
        for right in range(len(s)):
            dicti[s[right]]+=1
            while(sum(dicti.values())-max(dicti.values()))>k:
                dicti[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
            
            
            