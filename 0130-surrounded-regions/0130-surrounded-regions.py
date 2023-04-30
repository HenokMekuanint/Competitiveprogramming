class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited=[[False for i in range(len(board[0]))]for j in range(len(board))]
        
        def in_bound(row,col):
            return 0<=row<=len(board)-1 and 0<=col<=len(board[0])-1
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(row,col):
            if row==0 or row==len(board)-1 or col==0 or col==len(board[0])-1:
                is_border[0]=True
                return
            visited[row][col]=True
            components.append((row,col))
            for change_row,change_col in directions:
                new_row=row+change_row
                new_col=col+change_col
                if in_bound(new_row,new_col) and not visited[new_row][new_col] and board[new_row][new_col]=='O':
                    dfs(new_row,new_col)
            return components
        store=[]
        for row in range(1,len(board)-1):
            for col in range(1,len(board[0])-1):
                if not visited[row][col] and board[row][col]=="O":
                    components=[]
                    is_border=[False]
                    dfs(row,col)
                    if not is_border[0]:
                        store.extend(components)
        
        for row,col in store:
            board[row][col]='X'
            
                
        