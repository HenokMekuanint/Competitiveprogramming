from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        from collections import defaultdict
        graph=defaultdict(list)
        for i in range(len(adj)):
                graph[i].extend(adj[i])
        color=[0 for i in range(V)]
        ans=0
        def dfs(node,parent):
            nonlocal ans
            if color[node]==2:
                return True
            if color[node]==1:
                ans=1
                return False
            has_cycle=True
            color[node]=1
            for neighbour in graph[node]:
                if neighbour==parent:
                    continue
                has_cycle=has_cycle and dfs(neighbour,node)
                if not has_cycle:
                    return False


            color[node]=2
            return has_cycle
        
        for i in range(len(color)):
            if color[i]==0:
                rtn=dfs(i,-1)
                if not rtn:
                    return 1
        return ans
		    
		    


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends