class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        ans = defaultdict(float)
        
        def dp(row, col):
            nonlocal poured
            if row == 0 and col == 0:
                if poured>=1:
                    ans[(row,col)]=1
                return poured
            if row < 0 or col < 0:
                return 0
            
            if (row, col) in ans:
                return ans[(row, col)]
            
            if col > row:
                return 0
            
            
            
            left_champ = max(0, dp(row - 1, col - 1) - 1)
            right_champ = max(0, dp(row - 1, col) - 1)
            
            ans[(row, col)] = (left_champ + right_champ) / 2
            
            return ans[(row, col)]
        
        dp(query_row, query_glass)
        return min(1, ans[(query_row, query_glass)])
