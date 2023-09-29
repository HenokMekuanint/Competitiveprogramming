class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        graph=defaultdict(list)
        
        count=defaultdict(int)
        
        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        def dfs(node, end, path,visited):
            visited.add(node)
            if node == end:
                
                return path
            temp=[]
            for neighbour in graph[node]:
                if neighbour not in visited:
                    t=dfs(neighbour, end, path + [neighbour],visited)
                    if t!=[]:
                        return t

            return temp
        
        for start,end in trips:
            visited=set()
            temp=dfs(start,end,[start],set([start]))
            for node in temp:
                count[node]+=1
        memo=defaultdict(int)
        def dp(node,visited):
            including = (price[node]*count[node])/2
            without = price[node]*count[node]
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    inc,desc = dp(n,visited)
                    including+=desc
                    without+=min(inc,desc)
            return including,without
        
        return int(min(dp(0,set([0]))))
                        
            
            