class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[[]for col in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                ans[col].append(matrix[row][col])
        return ans
        