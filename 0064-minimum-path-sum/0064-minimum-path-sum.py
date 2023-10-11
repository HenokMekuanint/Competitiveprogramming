class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def in_bound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[row])
        directions=[(1,0),(0,1)]
        memo={}
        def dp(row,col):
            if row==len(grid)-1 and col==len(grid[row])-1:
                return grid[row][col]
            if (row,col) in memo:
                return memo[(row,col)]
            ans=float("inf")
            for change_row,change_col in directions:
                new_row=row+change_row
                new_col=col+change_col
                if in_bound(new_row,new_col):
                    ans=min(ans,dp(new_row,new_col)+grid[row][col])

            memo[(row,col)]=ans
            return memo[(row,col)]
        return dp(0,0)
        