class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        memo={}
        def dp(main_index,iner_index):
            if (main_index,iner_index) in memo:
                return memo[(main_index,iner_index)]
            if main_index==len(triangle)-1:
                return triangle[main_index][iner_index]
            
            memo[(main_index,iner_index)]=triangle[main_index][iner_index]+min(dp(main_index+1,iner_index+1),dp(main_index+1,iner_index))
            return memo[(main_index,iner_index)]
        return dp(0,0)
            
        