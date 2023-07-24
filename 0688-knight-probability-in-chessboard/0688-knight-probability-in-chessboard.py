class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        directions=[(-2,-1),(-2,1),(-1,-2),(1,-2),(-1,2),(1,2),(2,-1),(2,1)]
        
        def in_bound(row,col):
            nonlocal n
            return 0<=row<n and 0<=col<n
        
        ans=0
        if k==0 and in_bound(row,column):
            return 1
        elif k==0 and not in_bound(row,column):
            return 0
        memo=defaultdict(int)
        ans=0
        def dp(row,col,res,moves):
            
            if moves==k:
               
                return res
            if memo[(row,col,moves)]:
                return memo[(row,col,moves)]
            
            for change_row,change_col in directions:
                new_row=row+change_row
                new_col=col+change_col
                if in_bound(new_row,new_col):
                    memo[(row,col,moves)]+=dp(new_row,new_col,res/8,moves+1)
            return memo[(row,col,moves)]
        return dp(row,column,1,0)
                    
                
        
        
        