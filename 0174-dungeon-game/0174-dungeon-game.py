class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        directions=[(0,1),(1,0)]
        
        def in_bound(row,col):
            return 0<=row<len(dungeon) and 0<=col<len(dungeon[0])
        memo=defaultdict(lambda: float('inf'))
        def back_track(row,col):
            if row==len(dungeon)-1 and col==len(dungeon[0])-1:
                if dungeon[row][col]<0:
                    memo[(row,col)]=(-1*dungeon[row][col])+1
                    
                else:
                    memo[(row,col)]=1
                return memo[(row,col)]

            if memo[(row,col)]!=float("inf"):
                return memo[(row,col)]
                
            cur_min=float("inf")
            for change_row,change_col in directions:
                new_row=row+change_row
                new_col=col+change_col
                if in_bound(new_row,new_col):
                    
                    cur_min=min(max(1,back_track(new_row,new_col)-dungeon[row][col]),cur_min)
                   
            if cur_min!=float("inf"):
                                    
                memo[(row,col)]=cur_min
                return memo[(row,col)]
            
        
            
            
            
        a=back_track(0,0)
        return a
                
            
            
        