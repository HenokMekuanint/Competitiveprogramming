class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}  # Dictionary to store computed results

        def coin(cur_amount):
            if cur_amount in memo:  # Check if solution already exists in memo
                return memo[cur_amount]

            if cur_amount == 0:  # Base case: amount reached 0
                return 0

            if cur_amount < 0:  # Invalid amount, return -1
                return -1

            min_coins = float("inf")  # Initialize with infinity

            for con in coins:
                remaining_amount = cur_amount - con
                remaining_coins = coin(cur_amount - con)
                if remaining_coins >= 0:
                    min_coins = min(min_coins, 1 + remaining_coins)

            if min_coins == float("inf"):  # No valid combination found
                memo[cur_amount] = -1
            else:
                memo[cur_amount] = min_coins

            return memo[cur_amount]

        return coin(amount)
                
                
                
        
        
        