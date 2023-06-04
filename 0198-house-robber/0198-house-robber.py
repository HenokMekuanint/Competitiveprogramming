class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def dp(index):
            if index in memo:
                return memo[index]
            
            if index>=len(nums):
                return 0
            if index==len(nums)-1:
                return nums[index]
            memo[index]=max(nums[index]+dp(index+2),dp(index+1))
            return memo[index]
        return max(dp(0),dp(1))
                
                
        