class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memo={}
        def dp(row,col):
            if col==0 or row==col:
                return 1
            if col<0 or col>row:
                return 0

            
            if (row,col) in memo:
                return memo[(row,col)]
            memo[(row,col)]=dp(row-1,col)+dp(row-1,col-1)
            return memo[(row,col)]
            
        ans=[]
        for i in range(rowIndex+1):
            temp=[]
            for j in range(i+1):
                temp.append(dp(i,j))
            ans.append(temp)
        return ans[rowIndex]
            
            
        