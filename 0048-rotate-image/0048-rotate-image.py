class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        [[1,2,3],[4,5,6],[7,8,9]]
        i=0
        j=0
        """
        matrix.reverse()
        for i in range(len(matrix)):
            
            for j in range(len(matrix[i])):
                
                if i>j:
                    matrix[i][j],matrix[j][i]=matrix[j][i], matrix[i][j]
        return matrix
                