class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for r in range(len(matrix)):
            if matrix[r][-1] > target and matrix[r][0]<target:
                if target in matrix[r]:
                    return True
                
            elif matrix[r][-1]==target or matrix[r][0]==target:
                return True
            elif matrix[r][-1] > target and matrix[r][0]>target:
                    return False
        