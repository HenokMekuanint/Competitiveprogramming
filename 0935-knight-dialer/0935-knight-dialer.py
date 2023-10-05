class Solution:
    def knightDialer(self, n: int) -> int:
        matrix = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["*", "0", "#"],
        ]
        directions = [(-2, 1), (-1, 2), (1, -2), (2, -1),
                      (1, 2), (2, 1), (-1, -2), (-2, -1)]

        def in_bound(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

        memo = defaultdict(int)

        def dp(row, col, move):
            if move == 0:
                return 1

            if (row, col, move) in memo:
                return memo[(row, col, move)]

            total_ways = 0
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if in_bound(new_row, new_col) and matrix[new_row][new_col] != "*" and matrix[new_row][new_col] != "#":
                    total_ways += dp(new_row, new_col, move - 1)

            memo[(row, col, move)] = total_ways
            return total_ways

        total_ways = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != "*" and matrix[i][j] != "#":
                    total_ways += dp(i, j, n - 1)

        return total_ways % (10**9 + 7)