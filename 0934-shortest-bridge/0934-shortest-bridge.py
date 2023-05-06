class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions=[(1,0),(-1,0),(0,-1),(0,1)]
        def in_bound(row,col):
            return 0<=row<=len(grid)-1 and 0<=col<=len(grid[0])-1
        def dfs(row,col):
            if (row,col,0) in visited:
                return
            visited.add((row,col,0))
            for change_row,change_col in directions:
                new_row=row+change_row
                new_col=col+change_col
                if in_bound(new_row,new_col) and (new_row,new_col) not in visited and grid[new_row][new_col]==1:
                    dfs(new_row,new_col)
            return list(visited)
        def bfs(comp):
            queue=deque(comp)
            seen=set([(row,col) for row,col,step in queue])
            while queue:
                row,col,step=queue.popleft()
                if grid[row][col]==1 and (row,col,0) not in visited:
                    return step-1
                for change_row,change_col in directions:
                    new_row=row+change_row
                    new_col=col+change_col
                    if in_bound(new_row,new_col) and (new_row,new_col) not in seen:
                        queue.append((new_row,new_col,step+1))
                        seen.add((new_row,new_col))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    visited=set()
                    connected=dfs(i,j)
                    return bfs(connected)
                    
                    
                        
                
            
        