class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        parent=defaultdict(int)
        for i in range(1,n+1):
            parent[i]=i
        rank=[0 for i in range(1,n+1)]
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
        for frm,to,dist in roads:
            union(frm,to)
        hena=sorted(roads,key=lambda x:x[2])
        ans=float("inf")
        for frm,to,dist in hena:
            if find(1)==find(n)==find(frm)==find(to):
                ans=min(ans,dist)
        return ans
        