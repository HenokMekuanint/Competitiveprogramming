class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {}
        
        def dp(cur_sum):
            if cur_sum == target:
                return 1
            if cur_sum > target:
                return 0
            if cur_sum in memo:
                return memo[cur_sum]
            
            count = 0
            for i in range(len(nums)):
                if cur_sum + nums[i] > target:
                    break
                count += dp(cur_sum + nums[i])
            
            memo[cur_sum] = count
            return count
        
        return dp(0)
    
            
             