class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        if len(grid)==1 and grid[0][0]==0:
            return 1
            
        directions=[(-1,-1),(1,0),(-1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1)]
        
        def in_bound(row,col):
            return 0<=row<=len(grid)-1 and 0<=col<=len(grid[0])-1
        
        def bfs(init_row,init_col):
            queue=deque([(init_row,init_col,[(init_row,init_col)])])
            visited=set([(init_row,init_col)])
            while queue:
                node=queue.popleft()
                
                row,col,path=node[0],node[1],node[2]
                for change_row,change_col in directions:
                    
                    new_row=row+change_row
                    new_col=col+change_col
                    if in_bound(new_row,new_col) and (new_row,new_col) not in visited and grid[new_row][new_col]==0:
                        visited.add((new_row,new_col))
                        new_path=path+[(new_row, new_col)]
                        queue.append((new_row,new_col,new_path))
                        if new_row==len(grid)-1 and new_col==len(grid[0])-1:
                            if new_path:
                                return len(new_path)
                            
            return -1
        return bfs(0,0)
                    
                    
        