class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        temp=0
        res=0
        for i in range(len(nums)):
            if i<len(nums)-2 and nums[i+2]-nums[i+1]==nums[i+1]-nums[i]:
                temp+=1
                res+=temp
            else:
                temp=0
        return res
                
            
            
            
            
            
            
            
        