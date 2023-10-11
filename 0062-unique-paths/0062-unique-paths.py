class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        
        def inbound(row,col):
            nonlocal m,n
            return 0<=row<m and 0<=col<n
        def dp(row,col):
            if not inbound(row,col):
                return 0
            if row==m-1 and col==n-1:
                return 1
            if (row,col) in memo:
                return memo[(row,col)]
            
            memo[(row,col)]=dp(row+1,col)+dp(row,col+1)
            return memo[(row,col)]
        return dp(0,0)