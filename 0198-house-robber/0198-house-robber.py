class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dp(i):
            
            if i == 0:
                
                return nums[i]
            if i == 1:
                return max(nums[0],nums[1])
            if memo[i] == -1:
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            return memo[i]
        n = len(nums)
        memo = [-1 for _ in range(n)]
        return dp(n - 1)
                
                
        