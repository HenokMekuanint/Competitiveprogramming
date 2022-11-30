class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]
        nums.sort()
        left=0
        right=1
        
        while right<len(nums):
            if nums[left]==nums[right]:
                left+=2
                right+=2
            elif nums[left]!=nums[right]: 
                return nums[left]
        return nums[left]
            
        
