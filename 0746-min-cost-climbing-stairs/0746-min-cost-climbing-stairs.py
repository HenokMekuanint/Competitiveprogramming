class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans=float("inf")
        memo=defaultdict(int)
        def dp(index):
            nonlocal ans
            if index==len(cost)-1:
                memo[index]=cost[index]
                return cost[index]
            if index>len(cost)-1:
                return 0
            
            if not memo[index]:
                memo[index]=cost[index]+min(dp(index+1),dp(index+2))
            return memo[index]
        dp(0)
        return min(memo[0],memo[1])
                
                
            
        