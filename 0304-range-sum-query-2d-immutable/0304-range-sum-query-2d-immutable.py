class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        
        self.matrix=matrix
        self.prefix=[[0 for i in range(len(self.matrix[0]))] for j in range(len(self.matrix))]
        total=0
        for i in range(len(matrix)):
            for j in range(len(self.matrix[i])):
                if i==0:
                    total+=self.matrix[i][j]
                    self.prefix[i][j]=total
                elif i!=0 and j==0:
                    self.prefix[i][j]=self.matrix[i][j]+self.prefix[i-1][j]
                else:
                    self.prefix[i][j]=self.matrix[i][j]+self.prefix[i][j-1]+self.prefix[i-1][j]-self.prefix[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1==0:
            col_sub=0
        else:
            col_sub=self.prefix[row2][col1-1]
        if row1==0:
            row_sub=0
        else:
            row_sub=self.prefix[row1-1][col2]
        if row1==0 or col1==0:
            dig_add=0
        else:
            dig_add=self.prefix[row1-1][col1-1]
        return self.prefix[row2][col2]-col_sub-row_sub+dig_add
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)