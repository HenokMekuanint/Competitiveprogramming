class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent=defaultdict(int)
        for i in range(len(stones)):
            parent[i]=i
        rank=[0 for i in range(len(parent))]
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
            
            if rank[parentY]==rank[parentY]:
                rank[parentX]+=1
            if rank[parentX]>rank[parentY]:
                parent[parentY]=parentX
            else:
                parent[parentX]=parentY
        for i in range(len(stones)):
            for j in range(len(stones)):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    union(i,j)
        return len(stones) -len(set(find(x) for x in parent))