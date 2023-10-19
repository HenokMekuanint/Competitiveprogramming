class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
        for frm in graph:
            graph[frm].sort(reverse=True)

        res = []
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            res.append(node)

        dfs("JFK")
        return res[::-1]






        
        
       
            
            
        