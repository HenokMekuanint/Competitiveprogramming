class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans=[i for i in range(n,0,-1)]
        n=len(ans)
        while n>1:
            for i in range(k-1):
                popped=ans.pop()
                ans.insert(0,popped)
            ans.pop()
            n-=1
        return ans[0]
        