class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = defaultdict(int)
        
        def dp(cur_sum):
            if cur_sum == 0:
                return 1
            if cur_sum < 0:
                return 0
            if cur_sum in memo:
                return memo[cur_sum]
            
            count = 0
            for num in nums:
                if cur_sum - num < 0:
                    break
                count += dp(cur_sum - num)
            
            memo[cur_sum] = count
            return count
        
        return dp(target)
    
            
             