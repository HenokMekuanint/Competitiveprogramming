class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        sumrow=defaultdict(list)
        sumcol=defaultdict(list)
        for r in range(len(grid)):
            num_ones=sum(grid[r])
            num_zeros=len(grid[r])-num_ones
            sumrow[r].append(num_ones)
            sumrow[r].append(num_zeros)
        for c in range(len(grid[0])):
            num_ones=0
            for j in range(len(grid)):
                num_ones+=grid[j][c]
            num_zeros=len(grid)-num_ones
            sumcol[c].append(num_ones)
            sumcol[c].append(num_zeros)
        ans=[grid[i] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                ans[i][j]=sumrow[i][0]-sumrow[i][1]+sumcol[j][0]-sumcol[j][1]
        return ans
            
        