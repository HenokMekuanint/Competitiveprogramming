class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        # arr=[ 1   ,   2   ]
        memo={}
        def dp(index,steps):
            nonlocal arrLen
            if steps==0 and index==0:
                return 1
            if (index<0 or index>=arrLen) or (steps==0 and index!=0):
                return 0
            if (index,steps) in memo:
                return memo[(index,steps)]
            
            memo[(index,steps)]=dp(index-1,steps-1)+dp(index,steps-1)+dp(index+1,steps-1)
            return memo[(index,steps)]
        return dp(0,steps)%((10**9)+7)
        