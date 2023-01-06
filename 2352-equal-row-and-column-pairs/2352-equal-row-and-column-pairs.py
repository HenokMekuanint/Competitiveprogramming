class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        import copy
        ans = copy.deepcopy(grid)
        counter=0
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                if i>j:
                    ans[i][j],ans[j][i]=ans[j][i],ans[i][j]
        for pair1 in grid:
            for pair2 in ans:
                if pair1==pair2:
                    counter+=1
        return counter
        