class Solution:
    def climbStairs(self, n: int) -> int:
        ans=[0]
        memo=defaultdict(int)
        def stair(n):
            if n<3:
                return n
            if not memo[n]:
                memo[n]=stair(n-1)+stair(n-2)
            return memo[n]
              
        return stair(n)
        