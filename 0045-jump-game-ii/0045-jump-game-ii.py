class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo={}
        
        def dp(index):
            if index>=len(nums)-1:
                return 0
                
            if index in memo:
                return memo[index]
            ans=float("inf")
            for i in range(1,nums[index]+1):
                ans=min(ans,dp(index+i)+1)
            memo[index]=ans
            return memo[index]
        return dp(0)
            
            