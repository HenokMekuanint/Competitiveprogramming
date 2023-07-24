class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = defaultdict(int)

        def dp(index, bought):
            if index >= len(prices):
                return 0
            
            if memo[(index, bought)]:
                return memo[(index, bought)]
            
            if not bought:
                memo[(index, bought)] = max(dp(index + 1, not bought) - prices[index], dp(index + 1, bought))
            else :
                memo[(index, bought)] = max(dp(index + 2, not bought) + prices[index], dp(index + 1, bought))
            
            return memo[(index, bought)]
      
        return dp(0, False) 
                
                
                
                
                
                
            