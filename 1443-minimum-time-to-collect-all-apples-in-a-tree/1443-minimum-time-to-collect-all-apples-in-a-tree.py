class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if not edges:
            return 0
        adj_list=defaultdict(list)
        for frm,to in edges:
            adj_list[frm].append(to)
            adj_list[to].append(frm)
        visited=[False for i in range(len(hasApple))]
        def dfs(node):
            if node not in adj_list:
                if hasApple[node]:
                    return 2
                else:
                    return 0
            visited[node]=True
            rtn=0
            for neighbour in adj_list[node]:
                if not visited[neighbour]:
                    rtn+=dfs(neighbour)
            if node and (hasApple[node] or (not hasApple[node] and rtn)):
                return 2+rtn
            if not node:
                return rtn
            return 0
        return dfs(0)
        