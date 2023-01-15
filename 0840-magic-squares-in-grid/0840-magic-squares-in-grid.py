class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        

        def columnsummer(matrix):
            col=[]
            for i in range(len(matrix[0])):
                summ=0
                for j in range(len(matrix)):
                    summ+=matrix[j][i]
                col.append(summ)
            if col[0]==col[1]==col[2]:
                return True
            else:
                False
        def rowsummer(matrix):
            row=[]
            for i in range(len(matrix)):
                summ=0
                for j in range(len(matrix[i])):
                    summ+=matrix[i][j]
                row.append(summ)
            if row[0]==row[1]==row[2]:
                return True
            else:
                False

        def diagonalsummer(matrix):
            sum1=sum2=0
            for i in range(3):
                sum1+=matrix[i][i]
                sum2+=matrix[i][len(matrix[0])-1-i]
            if sum1==sum2:
                return True
            else:
                False
        counter=0
        for i in range(len(grid)-2):
            for j in range(len(grid[i])-2):
                ans=[]
                check=set()
                dup=False
                for k in range(i,i+3):
                    temp=[]
                    for l in range(j,j+3):
                        if grid[k][l] in check or grid[k][l]>9 or grid[k][l]<1:
                            dup=True
                        else:
                            check.add(grid[k][l])
                        temp.append(grid[k][l])
                    ans.append(temp)
                if columnsummer(ans)==rowsummer(ans)==diagonalsummer(ans)==True and dup==False:
                    counter+=1

        return counter
                
                
        