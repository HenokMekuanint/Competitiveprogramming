class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [n-1]
                    
        graph=defaultdict(list)
        degree=[0 for i in range(n)]
        for frm,to in edges:
            graph[frm].append(to)
            graph[to].append(frm)
            degree[frm]+=1
            degree[to]+=1
        leaves=[i  for i in range(len(degree)) if degree[i]==1]
        def bfs(leaves):
            nonlocal n
            while n>2:
                new_leaves=[]
                
                for leaf in leaves:
                    
                    for neighbour in graph[leaf]:
                        degree[neighbour]-=1
                        if degree[neighbour]==1:
                            new_leaves.append(neighbour)
                            
                    del graph[leaf]
                n-=len(leaves)
                leaves=new_leaves
            return leaves
        return bfs(leaves)
                        
                
            
            
        
            
        
        