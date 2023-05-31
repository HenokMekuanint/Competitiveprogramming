class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        state=[[ 1 if i==0 or j==0 else 0 for i in range(n) ] for j in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                state[i][j]=state[i][j-1]+state[i-1][j]
        return state[-1][-1]
                        
        