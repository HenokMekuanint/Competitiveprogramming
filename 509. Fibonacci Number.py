class Solution:
    def fib(self, n: int) -> int:
            if n==0:
                return 0
            elif n==1:
                return 1
            n=self.fib(n-1)+self.fib(n-2)
            return n
