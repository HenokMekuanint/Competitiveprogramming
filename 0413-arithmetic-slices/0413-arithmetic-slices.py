class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        temp=[0 for i in range(len(nums))]
        for i in range(len(nums)):
            if i<len(nums)-2 and nums[i+2]-nums[i+1]==nums[i+1]-nums[i]:
                temp[i]+=1
                if i>0 and temp[i]!=0:
                    temp[i]+=temp[i-1]
        return sum(temp)
                
            
            
            
            
            
            
            
        