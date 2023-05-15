class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ans=-1
        color=[(0,0) for i in range(len(edges))]
        graph=defaultdict(list)
        for i in range(len(edges)):
            if edges[i]>-1:
                graph[i].append(edges[i])
        def dfs(node,step):
            nonlocal ans
            if color[node][0]==2:
                return True
            if color[node][0]==1:
                ans=max(ans,abs(step-color[node][1]))
                return
            color[node]=(1,step)
            for neighbour in graph[node]:
                dfs(neighbour,step+1)

            color[node]=(2,step)
            return ans
        
        for i in range(len(edges)):
            if color[i][0]==0:
                dfs(i,0)
        print(color)
        return ans
            
                
                
                
                
        