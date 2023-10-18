class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0 for i in range(n)] for j in range(n)]
        
        row_ptr=0
        col_ptr=0
        init_num=1
        while row_ptr<n and col_ptr<n and matrix[row_ptr][col_ptr]==0:
            
            while col_ptr<n and matrix[row_ptr][col_ptr]==0 :
                matrix[row_ptr][col_ptr]=init_num
                col_ptr+=1
                init_num+=1
            row_ptr+=1
            col_ptr-=1
            
            while row_ptr<n and matrix[row_ptr][col_ptr]==0:
                matrix[row_ptr][col_ptr]=init_num
                row_ptr+=1
                init_num+=1
            col_ptr-=1
            row_ptr-=1
            while col_ptr>-1 and matrix[row_ptr][col_ptr]==0:
                matrix[row_ptr][col_ptr]=init_num
                col_ptr-=1
                init_num+=1
            row_ptr-=1
            col_ptr+=1
            while row_ptr>-1 and matrix[row_ptr][col_ptr]==0 :
                matrix[row_ptr][col_ptr]=init_num
                row_ptr-=1
                init_num+=1
            col_ptr+=1
            row_ptr+=1
        return matrix
            
            
            
            
            
        
        
        
        