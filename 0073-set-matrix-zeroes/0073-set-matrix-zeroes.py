class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        
        Do not return anything, modify matrix in-place instead.
        
        
        """
        zeros=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zeros.append([i,j])
        for pair in zeros:
            incrow=decrow=row=pair[0]
            inccol=deccol=col=pair[1]
            while decrow>-1:
                matrix[decrow][col]=0
                decrow-=1
            while incrow<len(matrix):
                matrix[incrow][col]=0
                incrow+=1
            while deccol>-1:
                matrix[row][deccol]=0
                deccol-=1
            while inccol<len(matrix[0]):
                matrix[row][inccol]=0
                inccol+=1
        return matrix
    """
[   [1,1,1],
    [1,0,1],
    [1,1,1]]

    """
                
            
            