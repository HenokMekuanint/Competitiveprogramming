class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0])!=r*c:
            return mat
        ans=[[-1 for i in range(c)] for i in range(r)]
        temp=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp.append(mat[i][j])
        row=col=0
        for j in range(len(temp)):
            if j%c==0 and j!=0:
                row+=1
                ans[row][j%c]=temp[j]
            else:
                ans[row][j%c]=temp[j]
        return ans
        