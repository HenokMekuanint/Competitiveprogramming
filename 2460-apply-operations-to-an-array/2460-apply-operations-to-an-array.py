class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        [   1   ,   4   ,   0   ,   2   ,   0   ,   0]
        
        """
        
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                nums[i-1]*=2
                nums[i]=0
        right=left=0
        while right<len(nums):
            if right==left or (nums[left]==0 and nums[right]==0):
                right+=1
            elif nums[left]==0 and nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right+=1
            else:
                left+=1
                right+=1
        return nums
            
        