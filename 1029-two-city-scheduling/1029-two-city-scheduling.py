class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs=sorted(costs, key=lambda x: x[1] - x[0])
        ans=0
        ptr=0
        while ptr<len(costs)//2:
            ans+=costs[ptr][1]
            ptr+=1
        while ptr<len(costs):
            ans+=costs[ptr][0]
            ptr+=1
        return ans
            
    
                
        