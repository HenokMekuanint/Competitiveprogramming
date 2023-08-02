class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        zero = 0 
        num = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                num += board[i][j]
                num *=10
                if board[i][j] == 0:
                    zero = (i,j)
                    
        
        num //= 10
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        q = deque()
        newstr = str(num)
        if len(newstr) == 5:
            newstr = '0' + newstr
        q.append((zero[0],zero[1], newstr))
            
        seen = set()
        level = 0
        while q:
            
            for i in range(len(q)):
                
                i,j,state = q.popleft()
                
                if state in seen:
                    continue
                    
                if state == '123450':
                    return level
                
                seen.add(state)
                
                for x,y in directions:
                    newx, newy = x + i, y + j 
                    if newx >= 0 and newy >= 0 and newx < 2 and newy < 3:
                        
                        target = (newx * 3) + newy
                        original = (i * 3) + j
                        num = 0
                        for z in range(len(state)):
                            
                            if z == target:
                                num += 0
                                num *= 10
                            elif z == original:
                                num += int(state[target])
                                num *= 10 
                            else:
                                num += int(state[z])
                                num *= 10

                        num //= 10
                        newstr = str(num)
                        if len(newstr) == 5:
                            newstr = '0' + newstr
                        q.append((newx,newy,newstr))
                
            level +=1
                  

        
        return -1