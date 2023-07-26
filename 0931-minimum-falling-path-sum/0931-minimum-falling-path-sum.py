class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        def in_bound(row,col):
            return 0<=row<len(matrix) and 0<=col<len(matrix[0])
        memo=defaultdict(lambda: float('inf'))
        directions=[(1,-1),(1,0),(1,1)]
        def dp(row,col):
            if not in_bound(row,col):
                return float("inf")
            if row==len(matrix)-1:
                return matrix[row][col]
            if not in_bound(row,col):
                return float("inf")
            
            if memo[(row,col)]!=float("inf"):
                return memo[(row,col)]
            temp=float("inf")
            for trav_col in range(0,len(matrix[row])):
                dp(row+1,col+1)
                memo[(row,trav_col)]=min(dp(row+1,trav_col+1)+matrix[row][trav_col],dp(row+1,trav_col)+matrix[row][trav_col],dp(row+1,trav_col-1)+matrix[row][trav_col])
                temp=min(temp,memo[(row,trav_col)])
            return temp
        return dp(0,0)
            
        