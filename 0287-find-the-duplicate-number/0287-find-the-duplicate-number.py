class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            index=abs(num)-1
            if nums[index]<0:
                return index+1
            else:
                nums[index]*=-1
       
        
        