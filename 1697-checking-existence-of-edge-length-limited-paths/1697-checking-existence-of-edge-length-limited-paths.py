class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        class UnionFind:
            
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n
            
            def find(self, node):
                
                if self.parent[node] != node:
                    self.parent[node] = self.find(self.parent[node])
                return self.parent[node]
            
            def union(self, node1, node2):
                
                par1 = self.find(node1)
                par2 = self.find(node2)
                
                if par1 != par2:
                    
                    rank1 = self.rank[par1]
                    rank2 = self.rank[par2]
                    
                    if rank1 > rank2:
                        self.parent[par2] = par1
                    elif rank1 < rank2:
                        self.parent[par1] = par2
                    else:
                        self.rank[par1] += 1
                        self.parent[par2] = par1
        
        union_find = UnionFind(n)
        edgeList.sort(key = lambda x: x[2])
        queries = [q + [i] for i, q in enumerate(queries)]
        queries.sort(key = lambda x: x[2])

        edge_idx = 0
        query_idx = 0
        ans = [False] * len(queries)
        while query_idx < len(queries):
            v1_q, v2_q, _, ans_idx = queries[query_idx]
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < queries[query_idx][2]:
                v1, v2, _ = edgeList[edge_idx]
                union_find.union(v1, v2)
                edge_idx += 1
            ans[ans_idx] = union_find.find(v1_q) == union_find.find(v2_q)
            query_idx += 1
        return ans