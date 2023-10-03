class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs=sorted(costs, key=lambda x: x[1] - x[0])
        ans=0
        for i in range(len(costs)//2):
            ans+=(costs[i][1]+costs[i+len(costs)//2][0])
        return ans
        
            
    
                
        