def AfricanCrossword(matrix):
    from collections import defaultdict
    row_freq=[]
    col_freq=[]
    ans=[]
    for i in range(len(matrix)):
        dicti=defaultdict(int)
        for j in range(len(matrix[i])):
            dicti[matrix[i][j]]+=1
        row_freq.append(dicti)
    for i in range(len(matrix[0])):
        dicti2=defaultdict(int)
        for j in range(len(matrix)):
            dicti2[matrix[j][i]]+=1
        
        col_freq.append(dicti2)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if row_freq[i][matrix[i][j]]==1 and col_freq[j][matrix[i][j]]==1:
                ans.append(matrix[i][j])
    return ans
n,m=map(int,input().split())
mat=[[0 for i in range(m)]for i in range(n)]
for i in range(n):
    line=input()
    for j in range(len(line)):
        mat[i][j]=line[j]
val=AfricanCrossword(mat)
print("".join(val))
