class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        change=image.copy()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        visited=[[False for i in range(len(image[0]))] for i in range(len(image))]
        def is_bound(row,col):
            return (0<=row<len(image) and 0<=col<len(image[0]))
        def dfs(row,col):
            visited[row][col]=True
            for change_row,change_col in directions:
                new_row=row+change_row
                new_col=col+change_col
                
                if is_bound(new_row,new_col) and not visited[new_row][new_col] and image[new_row][new_col]==image[sr][sc]:
                    change[new_row][new_col]=color
                    dfs(new_row,new_col)
        dfs(sr,sc)
        change[sr][sc]=color
        return change
        