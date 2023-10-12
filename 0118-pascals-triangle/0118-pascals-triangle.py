class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        memo={}
        def dp(row,col):
            if col==0 or row==col:
                return 1
            if col<0 or col>row:
                return 0
            if (row,col) in memo:
                return memo[(row,col)]
            memo[(row,col)]=(dp(row-1,col-1)+dp(row-1,col))
            return memo[(row,col)]
        pascals_triangle = []
        for i in range(numRows):
            row_list=[]
            for j in range(i+1):
                row_list.append(dp(i,j))
            pascals_triangle.append(row_list)
        return pascals_triangle
            