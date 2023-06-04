class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        memo={}
        def dp(index,end):
            if index in memo:
                return memo[index]
            
            if index>=end:
                return 0
            if index==len(nums)-1:
                return nums[index]
            memo[index]=max(nums[index]+dp(index+2,end),dp(index+1,end))
            return memo[index]
        ans2=dp(1,len(nums)) 
        memo={}
        ans1=dp(0,len(nums)-1)
        return max(ans1,ans2)