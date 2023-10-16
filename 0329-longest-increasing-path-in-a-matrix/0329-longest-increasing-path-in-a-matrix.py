class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        
        if not matrix:
            
            
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):

            if memo[row][col]:

                return memo[row][col]

            for dr, dc in directions:

                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:

                    memo[row][col] = max(memo[row][col], dfs(new_row, new_col))

            memo[row][col] += 1
            return memo[row][col]

        res = 0
        for i in range(rows):
            for j in range(cols):

                res = max(res, dfs(i, j))

        return res

