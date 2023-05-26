class Solution:
    def fib(self, n: int) -> int:
        memo=defaultdict(int)
        def fibbonachi(n):
            if n==0:
                return 0
            if n==1:
                return 1
            
            if not memo[n]:
                memo[n]=fibbonachi(n-1)+fibbonachi(n-2)
            return memo[n]

        return fibbonachi(n)
        