class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        queue = deque()

        def check(r, c):
            return 0<=r<len(mat) and 0<=c<len(mat[0]) and (r,c) not in visited
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))
                else:
                    mat[i][j] = -1
        while queue:
            row, col = queue.popleft()
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if check(new_row, new_col):
                    mat[new_row][new_col] = mat[row][col] + 1
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
        return mat
        