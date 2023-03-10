class Solution:
    def balancedString(self, s: str) -> int:

        n = len(s)
        left, ans, c = 0, n, Counter(s) 
        
        for right in range(len(s)):                                
            c[s[right]] -= 1                                

            while left < n and 4*max(c.values()) <= n:      
                ans = min(ans, right-left+1)                
                c[s[left]] += 1 
                left += 1

        return ans
        
        
        
        