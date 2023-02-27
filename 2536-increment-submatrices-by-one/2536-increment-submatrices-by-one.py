class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix=[[0 for i in range(n)] for i in range(n)]
        for query in queries:
            row1=query[0]
            col1=query[1]
            row2=query[2]
            col2=query[3]
            
            for i in range(row1,row2+1):
                matrix[i][col1]+=1
                if col2+1<len(matrix[0]):
                    matrix[i][col2+1]-=1
        for i in range(len(matrix)):
            total=0
            for j in range(len(matrix[i])):
                total+=matrix[i][j]
                matrix[i][j]=total
        return matrix
                
                    
        