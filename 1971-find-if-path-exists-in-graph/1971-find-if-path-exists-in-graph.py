class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent=defaultdict(int)
        for i in range(n):
            parent[i]=i
        rank=[0 for i in range(n)]
        def find(x):
            compress=[]
            while x!=parent[x]:
                compress.append(x)
                x=parent[x]
            for node in compress:
                parent[node]=x
            return x
            
        def union(x,y):
            parentX=find(x)
            parentY=find(y)
            if parentX==parentY:return
            
            if rank[parentY]==rank[parentY]:
                rank[parentX]+=1
            if rank[parentX]>rank[parentY]:
                parent[parentY]=parentX
            else:
                parent[parentX]=parentY
        for frm,to in edges:
            union(frm,to)
        return find(source)==find(destination)
                
                
                
                
            
            