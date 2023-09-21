class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        ans=0
        cur_sum=0
        prev_sum=0
        for row in range(len(grid)-2):
            
            for col in range(len(grid[row])-2):
                if  col==0:
                    cur_sum=grid[row][col]+grid[row][col+1]+grid[row][col+2]+grid[row+1][col+1]+grid[row+2][col]+grid[row+2][col+1]+grid[row+2][col+2]
                    prev_sum=cur_sum
                    ans=max(ans,cur_sum)
                else:
                    
                    cur_sum=prev_sum+(grid[row][col+2]-grid[row][col-1]+grid[row+1][col+1]-grid[row+1][col]+grid[row+2][col+2]-grid[row+2][col-1])
                    prev_sum=cur_sum
                    ans=max(ans,cur_sum)

        return ans
                    
                    
                
                
                
                
                
            