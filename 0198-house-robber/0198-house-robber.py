class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(index):
            if index not in memo:
                if index==len(nums)-1:
                    memo[index]=nums[index]
                    return nums[index]
                
                memo[index]=nums[index]
                for i in range(index+2,len(nums)):
                    memo[index]=max(memo[index],dp(i)+nums[index])
                    
                
            return memo[index]
                
        for i in range(len(nums)):
            if i not in memo:
                dp(i)
        return max(memo.values())
                
                
        