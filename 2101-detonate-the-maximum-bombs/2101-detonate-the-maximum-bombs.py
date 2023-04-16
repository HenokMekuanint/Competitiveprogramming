class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        import math
        dicti=defaultdict(list)
        ans=0
        def in_range(owner,neighbour):
            dis=math.sqrt((owner[0]-neighbour[0])**2+(owner[1]-neighbour[1])**2)
            return dis<=owner[2]
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i!=j:
                    if in_range(bombs[i],bombs[j]):
                        dicti[i].append(j)
        if not dicti:
            return 1
        def dfs(vertex,visited):
            if vertex in visited:
                return
            visited.add(vertex)
            for neighbour in dicti[vertex]:
                dfs(neighbour,visited)
            return len(visited)
        temp=list(dicti.keys())
        for i in temp:
            ans=max(ans,dfs(i,set()))
        return ans
        
        