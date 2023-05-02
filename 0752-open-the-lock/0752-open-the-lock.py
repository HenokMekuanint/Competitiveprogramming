class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def bfs():
            queue=deque([("0000",0)])
            visited=set(deadends)
            while queue:
                node,step=queue.popleft()
                if node==target:return step
                if node in visited:
                    continue
                visited.add(node)
                for i in range(4):
                    if node[i]=="9":
                        inc_pattern=list(node)
                        inc_pattern[i]="1"
                        inc_com="".join(inc_pattern)
                        if inc_com not in visited:queue.append((inc_com,step+1))
                    else:
                        inc_pattern=list(node)
                        inc_pattern[i]=str(int(inc_pattern[i])+1)
                        inc_com="".join(inc_pattern)
                        if inc_com not in visited:queue.append((inc_com,step+1))
                    if node[i]=="0":
                        dec_pattern=list(node)
                        dec_pattern[i]="9"
                        dec_com="".join(dec_pattern)
                        if dec_com not in visited:queue.append((dec_com,step+1))
                    else:
                        dec_pattern=list(node)
                        dec_pattern[i]=str(int(dec_pattern[i])-1)
                        dec_com="".join(dec_pattern)
                        if dec_com not in visited:queue.append((dec_com,step+1))
            return -1
        return bfs()
                        
                        
                        
                        
                    
                
            