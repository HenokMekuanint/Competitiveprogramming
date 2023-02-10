class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        while left<right:
            cursum=nums[right]+nums[left]
            if cursum>target:
                right-=1
            elif cursum<target:
                left+=1
            else:
                return [left+1,right+1]