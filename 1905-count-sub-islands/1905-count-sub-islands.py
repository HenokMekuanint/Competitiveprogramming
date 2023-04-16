class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ans=0
        visited=[[False for i in range(len(grid1[0]))]for j in range(len(grid1))]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def is_inbound(row,col):
            return 0<=row<len(grid1) and 0<=col<len(grid1[0])
        
        def dfs(row,col):
            visited[row][col]=True
            colls.append([row,col])
            
            for change_row,change_col in directions:
                new_row=row+change_row
                new_col=col+change_col
                if is_inbound(new_row,new_col) and not visited[new_row][new_col] and grid2[new_row][new_col]==1:
                    dfs(new_row,new_col)
            return colls
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col]==1 and not visited[row][col]:
                    flag=True
                    colls=[]
                    dfs(row,col)
                    for check_row ,check_col in colls:
                        if grid1[check_row][check_col]==0:
                            flag=False
                            break
                    if flag:ans+=1
                    
        return ans
            
        