class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
# [ 2 , 3 , 3 , 6]        
#       L
#    R
        nums.sort()
        ans=0
        for cur in range(len(nums)-2):
            left=cur+1
            right=cur+2
            if nums[cur]+nums[left]>nums[right] and nums[cur]+nums[right]>nums[left] and nums[right]+nums[left]>nums[cur]:
                    ans=max(ans,nums[cur]+nums[left]+nums[right])
        return ans
        