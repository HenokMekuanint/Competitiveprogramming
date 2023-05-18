class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent=defaultdict(int)
        for i in range(1,len(edges)+1):
            parent[i]=i
        rank=[0 for i in range(len(edges))]
        def find(x):
            root=x
            while root!=parent[root]:
                root=parent[root]
            
            while x!=root:
                temp=parent[x]
                parent[x]=root
                x=temp
            return root
            
        def union(x,y):
            parentX=find(x)
            parentY=find(y)
            if parentX==parentY:return
            
            if rank[parentY-1]==rank[parentY-1]:
                rank[parentX-1]+=1
            if rank[parentX-1]>rank[parentY-1]:
                parent[parentY]=parentX
            else:
                parent[parentX]=parentY
        for frm,to in edges:
            if find(frm)==find(to):
                return [frm,to]
            union(frm,to)