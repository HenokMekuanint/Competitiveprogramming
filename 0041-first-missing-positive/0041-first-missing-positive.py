class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ptr=0
        for i in range(len(nums)):
            if nums[i]>0:
                nums[ptr]=nums[i]
                ptr+=1
        nums=set(nums[:ptr])
        if not nums:
            return 1
        max_num=max(nums)
        for i in range(1,max_num+2):
            if i not in nums:
                return i
        
        
        
        