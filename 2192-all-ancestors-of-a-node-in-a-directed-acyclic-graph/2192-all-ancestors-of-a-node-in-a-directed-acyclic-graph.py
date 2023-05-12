class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)
        indegree=[0 for i in range(n)]
        for frm,to in edges:
            graph[frm].append(to)
            indegree[to]+=1
        init_nodes=[node for node in range(len(indegree)) if indegree[node]==0]

        ans=[set() for i in range(n)]
        def bfs(nodes):

            queue=deque(nodes)
            
            while queue:
                node=queue.popleft()
                
                for neighbour in graph[node]:
                    indegree[neighbour]-=1
                    ans[neighbour].add(node)
                    ans[neighbour]=ans[neighbour].union(ans[node])
                    if not indegree[neighbour]:
                        queue.append(neighbour)
     
            for i in range(len(ans)):
                ans[i]=sorted(list(ans[i]))
            return ans
        return bfs(init_nodes)      
 
        
        