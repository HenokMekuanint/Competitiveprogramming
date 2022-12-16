class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        for r in range(len(grid)-2):
                _sum=0
                right=left=0
                while right<left+3:
                    _sum+=grid[r][right]
                    _sum+=grid[r+2][right]
                    right+=1
                _sum+=grid[r+1][left+1]
                right-=1
                ans = max(ans, _sum)
                while right<len(grid[r])-1:
                    _sum-=grid[r][left]
                    _sum-=grid[r+2][left]
                    _sum-=grid[r+1][left+1]
                    left+=1
                    _sum+=grid[r][right+1]
                    _sum+=grid[r+1][right]
                    _sum+=grid[r+2][right+1]
                    right+=1
                    ans = max(ans, _sum)
        return ans

            
            
            
            
            
            