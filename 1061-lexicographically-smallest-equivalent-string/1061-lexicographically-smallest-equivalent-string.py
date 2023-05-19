class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent=defaultdict(str)
        for i in range(ord("a"),ord("z")+1):
            parent[chr(i)]=chr(i)
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
            
            if parentX>parentY:
                parent[parentX]=parentY
            else:
                parent[parentY]=parentX
        for i in range(len(s1)):
            union(s1[i],s2[i])
        ans=""
        for char in baseStr:
            ans+=find(char)
        return ans
