class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
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
                parent[parentY]=parentX
            else:
                parent[parentX]=parentY
        for equation in equations:
            if equation[1]=="=":
                union(equation[0],equation[-1])
        for equation in equations:
            if equation[1]=="!":
                if find(equation[0])==find(equation[-1]):
                    return False
        return True