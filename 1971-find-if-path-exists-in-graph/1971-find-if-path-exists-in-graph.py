class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dicti=defaultdict(list)
        for neigh1,neigh2 in edges:
            dicti[neigh1].append(neigh2)
            dicti[neigh2].append(neigh1)
        def dfs(vertex,visited):
            nonlocal destination
            if  vertex==destination:
                return True
            visited.add(vertex)
            found=False
            for neighbour in dicti[vertex]:
                if neighbour not in visited:
                    found= found or dfs(neighbour, visited)
                    if found:
                        return found
    
            return found
        return dfs(source,set())