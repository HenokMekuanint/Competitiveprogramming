class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:return 0
        nums.sort()
        ans=float("inf")
        ans=min(ans,max(nums[3:])-min(nums[3:]))
        ans=min(ans,max(nums[:-3])-min(nums[:-3]))
        ans=min(ans,max(nums[2:-1])-min(nums[2:-1]))
        ans=min(ans,max(nums[1:-2])-min(nums[1:-2]))
        return ans
            
            
        