class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner=defaultdict(int)
        loser=defaultdict(int)
        ans=[[],[]]
        for pair in matches:
            winner[pair[0]]+=1
            loser[pair[1]]+=1
        for losers in loser:
            if loser[losers]==1:
                ans[1].append(losers)
        coll=set(loser.keys())
        for winners in winner:
            if winners not in coll:
                ans[0].append(winners)
        ans[0].sort()
        ans[1].sort()
        return ans
        