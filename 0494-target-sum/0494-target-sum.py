class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dp(index, cur_sum):
            nonlocal target
            
            if index == len(nums):
                if cur_sum == target:
                    return 1
                return 0
            
            if (index, cur_sum) in memo:
                return memo[(index, cur_sum)]
            
            ways = dp(index + 1, cur_sum + nums[index]) + dp(index + 1, cur_sum - nums[index])
            memo[(index, cur_sum)] = ways
            
            return ways
        
        return dp(0, 0)
                
        