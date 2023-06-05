class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def findMaxProfit(index,max_profit,min_far):
            if index>=len(prices):
                return max_profit
            cost=prices[index]-min_far
            max_profit=max(max_profit,cost)
            min_far=min(min_far,prices[index])
            return findMaxProfit(index+1,max_profit,min_far)



        maxProfit = findMaxProfit(1,0,prices[0])
        return(maxProfit)



        
        