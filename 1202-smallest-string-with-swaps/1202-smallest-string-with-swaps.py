class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        parent=defaultdict(int)
        for i in range(len(s)):
            parent[i]=i
        rank=[0 for i in range(len(s))]
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
        for index1,index2 in pairs:
            union(index1,index2)
        collections=defaultdict(list)
        for i in range(len(s)):
            collections[find(i)].append((s[i],i))
        ans=['' for i in range(len(s))]
        for key in collections:
            collections[key]=deque(sorted(collections[key]))
        for i in range(len(s)):
            p=find(i)
            ans[i]=collections[p][0][0]
            collections[p].popleft()
        return "".join(ans)
            
            
        
        
        
        