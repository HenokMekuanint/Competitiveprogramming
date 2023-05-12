class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph=defaultdict(list)
        indegree=[0 for i in range(len(quiet))]
        for frm,to in richer:
            graph[frm].append(to)
            indegree[to]+=1
        init_nodes=[i for i in range(len(indegree)) if indegree[i]==0]
        ans=[i  for  i in range(len(indegree)) ]
        def bfs(nodes):
            queue=deque(nodes)
            
            while queue:
                node=queue.popleft()
                
                for neighbour in graph[node]:
                    indegree[neighbour]-=1
                    if quiet[ans[neighbour]]>quiet[ans[node]]:
                        ans[neighbour]=ans[node]
                    if indegree[neighbour]==0:
                        queue.append(neighbour)
            return ans
        return bfs(init_nodes)
                        
                
        