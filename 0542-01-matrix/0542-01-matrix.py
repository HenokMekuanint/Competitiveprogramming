class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def in_bound(row,col):
            return 0<=row<=len(mat)-1 and 0<=col<=len(mat[0])-1
        
        ans=[[float("inf") for i in range(len(mat[0]))]for j in range(len(mat))]
        queue=deque()
        for r in range(len(mat)):
            for c in range(len(mat[r])):
                if mat[r][c]==0:
                    ans[r][c]=0
                    queue.append((r,c))
        def bfs():
            while queue:
                row,col=queue.popleft()
                
                for change_row,change_col in directions:
                    new_row=row+change_row
                    new_col=col+change_col
                    if in_bound(new_row,new_col) and ans[new_row][new_col]>ans[row][col]+1:
                        ans[new_row][new_col]=ans[row][col]+1
                        queue.append((new_row,new_col))
            return ans
        return bfs()
    
                
                
            
            
        