class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        orderedPiles =[]
        sum = 0
        start = 0
        end = len(piles) -1
        while start < end :
            subPiles = []
            subPiles.append(piles[start])
            subPiles.append(piles[end])
            end -=1
            subPiles.append(piles[end])
            start += 1
            end -= 1
            orderedPiles.append(subPiles)
        for i in orderedPiles:
            sum += i[-1]
        return sum
