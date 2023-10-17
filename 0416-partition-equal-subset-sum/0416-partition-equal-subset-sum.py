class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arrsum=sum(nums)
        if arrsum%2!=0:
            return False
        memo={}
        
        def dp(index,summission):
            state=(index,summission)
            
            if index>=len(nums):
                if 2*summission==arrsum:
                    return True
                else:
                    return False
                
            if state in memo:
                return memo[state]
            memo[state]=False
            memo[state]=dp(index+1,summission+nums[index]) or dp(index+1,summission)
            return memo[state]
        return dp(0,0)
            
            
                
        