class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(matrix[0])):
            array=[]
            for j in range(len(matrix)):
                array.append(matrix[j][i])
            ans.append(array)
        return ans