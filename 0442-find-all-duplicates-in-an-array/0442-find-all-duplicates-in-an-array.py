class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        counter=0
        for num in nums:
            index=abs(num)-1
            if nums[index]<0:
                ans.append(index+1)
            else:
                nums[index]*=-1
        return ans
                
                
        