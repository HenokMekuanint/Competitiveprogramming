class Solution:
    def racecar(self, target: int) -> int:
        
        def bfs(target):
            queue=deque([(0,0,1)])
            visited=set([(0,1)])
            while queue:
                move,position,speed=queue.popleft()
                if position==target:
                    return move
                for i in range(1):
                    acc_pos=position+speed
                    acc_speed=2*speed
                    if speed>0:
                        dec_speed=-1
                    else:
                        dec_speed=1
                    if (acc_pos,acc_speed) not in visited:
                        queue.append((move+1,acc_pos,acc_speed))
                        visited.add((acc_pos,acc_speed))
                    if (position,dec_speed) not in visited:
                        queue.append((move+1,position,dec_speed))
                        visited.add((position,dec_speed))
        ans=bfs(target)
        return ans
                
        