class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        ans=float("-inf")
        ith_value=values[0]
        for j in range(1,len(values)):
            jth_value=values[j]-j
            ans=max(ans,ith_value+jth_value)
            ith_value=max(ith_value,values[j]+j)
        return ans
        