class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        memo=defaultdict(int)
        def dp(index,count):
            if index==len(satisfaction):
                return 0
            if memo[(index,count)]:
                return memo[(index,count)]     
            memo[(index,count)]=max((satisfaction[index]*count)+dp(index+1,count+1),dp(index+1,count))
            return memo[(index,count)]
        return dp(0,1)
    
        