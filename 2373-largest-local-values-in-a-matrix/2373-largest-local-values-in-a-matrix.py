class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans=[[ -1 for i in range(0,len(grid)-2)] for i in range(0,len(grid)-2)]
        for i in range(len(grid)-2):
            for j in range(len(grid[i])-2):
                loc_max=grid[i][j]
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        loc_max=max(loc_max,grid[k][l])
                ans[i][j]=loc_max
        return ans
        