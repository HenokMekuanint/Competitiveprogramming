class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        memo={}
        def dp(index,buy):
            nonlocal fee
            if index>=len(prices):
                return 0
            
            
            if (index,buy) in memo:
                return memo[(index,buy)]
            
            if buy:
                memo[(index,buy)]=max(-prices[index]+dp(index+1,0),0+dp(index+1,1))
            else:
                memo[(index,buy)]=max(prices[index]+dp(index+1,1)-fee,0+dp(index+1,0))
            return memo[(index,buy)]
        return dp(0,1)
        