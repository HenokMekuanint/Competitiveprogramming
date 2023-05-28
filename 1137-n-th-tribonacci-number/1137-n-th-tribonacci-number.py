class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo=defaultdict(int)
        
        def tribonacci(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n==2:
                return 1
            if not memo[n]:
                memo[n]=tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
            return memo[n]
        return tribonacci(n)
        