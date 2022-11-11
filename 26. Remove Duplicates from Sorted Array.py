class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=1
        while right<len(nums):
            if nums[right]==nums[left]:
                nums.pop(right)
            else:
                left=right
                right+=1
        return len(nums)
        
