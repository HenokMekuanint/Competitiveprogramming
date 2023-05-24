class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        temp=[1]*numOnes
        temp+=[0]*numZeros
        temp+=[-1]*numNegOnes
        ans=0
        left=0
        while k:
            ans+=temp[left]
            left+=1
            k-=1
        return ans
            
            
            
        