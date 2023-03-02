class Solution:
    from collections import deque
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        queue=deque()
        for i in range(len(tickets)):
            queue.append(i)
        num_dec=tickets[k]
        while tickets[k]!=0:
            complete_cycle=len(tickets)
            while complete_cycle>0 and tickets[k]>0:
                popped_index=queue.popleft()
                if tickets[popped_index]>0:
                    tickets[popped_index]-=1
                    queue.append(popped_index)
                    time+=1
                else:
                    queue.append(popped_index)
                complete_cycle-=1
        return time
                
            