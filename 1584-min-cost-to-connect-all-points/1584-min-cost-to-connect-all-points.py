class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent=defaultdict(int)
        for i in range(len(points)):
            parent[i]=i
        rank=[0 for i in range(len(points))]
        def find(x):
            root=x
            while root != parent[root]:
                root = parent[root]
            while root!=x:
                temp=parent[x]
                parent[x]=root
                x=temp
            return root
            
        def union(x,y):
            parentX=find(x)
            parentY=find(y)
            if parentX==parentY:return
            
            if rank[parentX] == rank[parentY]:
                rank[parentX]+=1
            if rank[parentX] > rank[parentY]:
                parent[parentY] = parentX
            else:
                parent[parentX] = parentY
        ans=0
        minheap = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                p1=points[i]
                p2=points[j]
                dist=abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
                minheap.append((dist,i,j))
        heapify(minheap)
        while len(minheap)>0:
            dis, p1, p2 = heappop(minheap)
            if find(p1) != find(p2):
                union(p1,p2)
                ans += dis
            
        return ans
        