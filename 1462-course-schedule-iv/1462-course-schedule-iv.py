class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph=defaultdict(list)
        childrens=defaultdict(set)
        indegree=[0 for i in range(numCourses)]
        for frm,to in prerequisites:
            graph[frm].append(to)
            indegree[to]+=1
        init_nodes=[i for i in range(numCourses) if indegree[i]==0]
        ans=[False for i in range(len(queries))]
        def bfs(nodes):
            queue=deque(nodes)
            while queue:
                node=queue.popleft()
                for neighbour in graph[node]:
                    indegree[neighbour]-=1
                    childrens[node].add(node)
                    childrens[neighbour]=childrens[neighbour].union(childrens[node])
                    if not indegree[neighbour]:
                        
                        queue.append(neighbour)
            return childrens
        bfs(init_nodes)
        for i in range(len(queries)):
            child,parent=queries[i][0],queries[i][1]
            if child in childrens[parent]:
                ans[i]=True
        return ans
                    
                
                
        
        
        