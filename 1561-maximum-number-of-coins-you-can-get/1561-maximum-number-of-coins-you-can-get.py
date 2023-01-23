class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left=0
        right=len(piles)-2
        ans=0
        while left<right:
            ans+=piles[right]
            left+=1
            right-=2
        return ans
        