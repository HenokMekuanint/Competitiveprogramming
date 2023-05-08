class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=defaultdict(int)
        graph=defaultdict(list)
        for to,frm in prerequisites:
            graph[frm].append(to)
            indegree[to]+=1
        temp=[]
        for  i in range(numCourses):
            if not indegree[i]:
                temp.append(i)
        def bfs(nodes):
            queue=deque(nodes)
            visited=set()
            while queue:
                node=queue.popleft()
                visited.add(node)
                for neighbour in graph[node]:
                    indegree[neighbour]-=1
                    if not indegree[neighbour]:
                        queue.append(neighbour)
            if len(visited)==numCourses:
                return True
            else:
                return False
        return bfs(temp)
                        
                