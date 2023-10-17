class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [[-1] * (sum(nums) + 1) for _ in range(n)]
        arrsum=sum(nums)
        def dp(index,summission):
            nonlocal arrsum
            if index>=len(nums):
                if 2*summission==arrsum:
                    return True
                else:
                    return False
            if memo[index][summission] != -1:
                return memo[index][summission]

            memo[index][summission] = dp(index + 1, summission + nums[index]) or dp(index + 1, summission)
            return memo[index][summission]
        return dp(0,0)
            
            
                
        