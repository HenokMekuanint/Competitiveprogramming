class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_graph=defaultdict(list)
        safe_nodes=set()
        for i in range(len(graph)):
            adj_graph[i].extend(graph[i])
        
        color = [0 for i in range(len(graph))]
        def dfs(node):
            if color[node] == 2:
                return True
            if color[node] == 1:
                return False
            
            is_safe = True
            color[node] = 1
            for neighbour in adj_graph[node]:
                is_safe = is_safe and dfs(neighbour)
                if not is_safe:
                    return False
            
            color[node] = 2
            return is_safe
        for key in adj_graph:
            if color[key] == 0:
                dfs(key)
        
        ans = [node for node in adj_graph if color[node] == 2]
        ans.sort()
        return ans
        
            
            
        