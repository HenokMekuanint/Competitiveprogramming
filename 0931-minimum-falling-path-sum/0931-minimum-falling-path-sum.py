class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        def in_bound(row,col):
            return 0<=row<len(matrix) and 0<=col<len(matrix[0])
        memo=defaultdict(lambda: float('inf'))
        def dp(row,col):
            if not in_bound(row,col):
                return float("inf")
            if row==len(matrix)-1:
                return matrix[row][col]
            
            if memo[(row,col)]!=float("inf"):
                return memo[(row,col)]
            temp=float("inf")
            memo[(row,col)]=min(dp(row+1,col-1)+matrix[row][col],dp(row+1,col)+matrix[row][col],dp(row+1,col+1)+matrix[row][col])
            return memo[(row,col)]
        ans=float("inf")
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ans=min(ans,dp(i,j))
            break
       
        return ans
            
        