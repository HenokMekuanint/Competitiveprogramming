class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        temp=[]
        ans=0
        for i in range(numOnes):
            temp.append(1)
        for i in range(numZeros):
            temp.append(0)
        for i in range(numNegOnes):
            temp.append(-1)
        left=0
        while k:
            ans+=temp[left]
            left+=1
            k-=1
        return ans
            
            
            
        