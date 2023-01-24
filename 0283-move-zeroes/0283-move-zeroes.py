class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        [0,1,0,3,12]
         L
           R
        
        """
        right=left=0

        while right<len(nums):
            if nums[right]==0 and nums[left]==0:
                right+=1
            elif nums[left]==0 and nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right+=1
            else:
                left+=1
                right+=1
        
        