class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=set()
        dicti=defaultdict(list)
        ans=0
        for row in range(len(isConnected)):
            for col in range(len(isConnected)):
                dicti[row+1]
                if col!=row and isConnected[row][col]==1:
                    dicti[row+1].append(col+1)
        def dfs(vertex):
            
            
            visited.add(vertex)
            
            for neighbour in dicti[vertex]:
                if neighbour not in visited:
                    dfs(neighbour)
        for v in dicti:
            if v not in visited:
                dfs(v)
                ans+=1
        return ans
                    
                    