class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        memo = {}
        memo[0] = 0
        memo[1] = 1
        if n in memo:
            return n
        def getmax(n):
            if n not in memo:
                if n % 2 != 0:
                    memo[n] = getmax(n // 2) + getmax((n // 2) + 1)
                else:
                    memo[n] = getmax(n // 2)
            return memo[n]
        
        for i in range(n + 1):
            if i not in memo:
                getmax(i)
        
        return max(memo.values())
        
        
            
        