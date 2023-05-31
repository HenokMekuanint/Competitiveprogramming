class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]==1 or obstacleGrid[0][0]==1 :return 0
        state=[[ 0 for j in range(len(obstacleGrid[i]))] for i in range(len(obstacleGrid))]
        state[-1][-1]=1
        for i in range(len(obstacleGrid)-1,-1,-1):
            j=len(obstacleGrid[i])-1
            while obstacleGrid[i][j]!=1 and j>-1:
                state[i][j]=1
                j-=1
            break
        for j in range(len(obstacleGrid[0])-1,-1,-1):
            i=len(obstacleGrid)-1
            
            while obstacleGrid[i][j]!=1 and  i>-1:
                state[i][j]=1
                i-=1
            break
        for i in range(len(obstacleGrid)-2,-1,-1):
            for j in range(len(obstacleGrid[i])-2,-1,-1):
                if obstacleGrid[i][j]!=1:
                        state[i][j]=state[i][j+1]+state[i+1][j]
        return state[0][0]
