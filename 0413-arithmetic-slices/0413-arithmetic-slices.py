class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        memo = {}

        def slices(idx):
            if idx in memo:
                return memo[idx]
            if idx >= len(A) - 2:
                return 0
            dp = 0
            if A[idx + 2] - A[idx + 1] == A[idx + 1] - A[idx]:
                dp = 1 + slices(idx + 1)
            slices(idx + 1)  # Ensure to call the function to reset the count
            memo[idx] = dp
            return dp

        count = 0
        for i in range(len(A)):
            count += slices(i)
        return count

            
            
            
            
            
            
            
        