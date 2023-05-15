from typing import List


from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        from collections import defaultdict
        graph=defaultdict(list)
        indegree=[0 for i in range(n)]
        for frm,to in edges:
            graph[frm].append(to)
            indegree[to-1]+=1
        init_nodes=[(i+1,1) for i in range(len(indegree)) if indegree[i]==0]
        ans=[1 if indegree[i]==0 else 0 for i in range(n)]
        def bfs(nodes):
            from collections import deque
            queue=deque(nodes)
            
            while queue:
                node,step=queue.popleft()
                
                for neighbour in graph[node]:
                    indegree[neighbour-1]-=1
                    if not indegree[neighbour-1]:
                        ans[neighbour-1]=step+1
                        queue.append((neighbour,step+1))
            return " ".join(map(str,ans))
        
        return bfs(init_nodes)
