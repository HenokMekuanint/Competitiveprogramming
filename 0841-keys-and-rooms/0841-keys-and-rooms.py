class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        indexes={i for i in range(len(rooms))}
        dicti=defaultdict(list)
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                dicti[i].append(rooms[i][j])
        
        def bfs(vertex):
            visited=set([vertex])
            queue=deque([vertex])
            indexes.remove(vertex)
            while queue:
                node=queue.popleft()
                for neighbour in dicti[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                        indexes.remove(neighbour)
            return len(indexes)==0
        return bfs(0)
        
                
        