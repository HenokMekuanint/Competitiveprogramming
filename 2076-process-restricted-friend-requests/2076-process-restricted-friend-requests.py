class UF:
    def __init__(self, n):
        self.parents = list(range(n))
        
    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u, v):
        x, y = self.find(u), self.find(v)
        if x != y:
            self.parents[y] = x
            return x
        return -1
		
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf, ban, group, ans = UF(n), defaultdict(set), {i: {i} for i in range(n)}, []
        for u, v in restrictions:
            ban[u].add(v)
            ban[v].add(u)
        for u, v in requests:
            p, q = uf.find(u), uf.find(v)
            if p == q:
                ans.append(True)
                continue
            if group[p] & ban[q] or group[q] & ban[p]:
                ans.append(False)
                continue
            p = uf.union(u, v)
            group[p] |= group[q]
            ban[p] |= ban[q]
            ans.append(True)
        return ans