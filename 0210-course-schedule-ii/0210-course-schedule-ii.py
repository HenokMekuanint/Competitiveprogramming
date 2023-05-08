class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree=defaultdict(int)
        graph=defaultdict(list)
        for to,frm in prerequisites:
            indegree[to]+=1
            graph[frm].append(to)
        temp=[]
        for key in range(numCourses):
            if indegree[key]==0:
                temp.append(key)
        def bfs(inp):
            nonlocal numCourses
            queue=deque(inp)
            visited=list()
            while queue:
                node=queue.popleft()
                visited.append(node)
                for neighbour in graph[node]:
                    indegree[neighbour]-=1
                    if indegree[neighbour]==0:
                        queue.append(neighbour)
            print(visited)
            if len(visited)==numCourses:
                return visited
            else:
                []
        return bfs(temp)
            
            
        