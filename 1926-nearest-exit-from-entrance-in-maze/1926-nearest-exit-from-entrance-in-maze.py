class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        direcions=[(1,0),(0,1),(-1,0),(0,-1)]
        
        def in_bound(row,col):
            return 0<=row<=len(maze)-1 and 0<=col<=len(maze[0])-1
        def in_border(row,col):
            if row==0 or col==0 or row==len(maze)-1 or col==len(maze[0])-1:
                return True
            return False
            
        def bfs(init_row,init_col):
            queue=deque([(init_row,init_col,0)])
            visited=set([init_row,init_col])
            while queue:
                node=queue.popleft()
                row,col,step=node[0],node[1],node[2]
                if in_border(row,col) and (row!=init_row or col!=init_col):
                    return step
                for change_row,change_col in direcions:
                    new_row=row+change_row
                    new_col=col+change_col
                    if in_bound(new_row,new_col) and (new_row,new_col) not in visited and maze[new_row][new_col]==".":
                        queue.append((new_row,new_col,step+1))
                        visited.add((new_row,new_col))
            return -1
        return bfs(entrance[0],entrance[1])
        