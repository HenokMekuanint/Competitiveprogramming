class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName=kingName
        self.parent_childs=defaultdict(list)
        self.is_dead=defaultdict(lambda:False)
        self.parent_childs[kingName]=[]
    def birth(self, parentName: str, childName: str) -> None:
        self.parent_childs[parentName].append(childName)
    def death(self, name: str) -> None:
        self.is_dead[name]=True
    def getInheritanceOrder(self) -> List[str]:
        ans=[]
        def dfs(vertex):
            if not self.is_dead[vertex]:
                ans.append(vertex)
            if not self.parent_childs[vertex]:
                return
            for neighbour in self.parent_childs[vertex]:
                dfs(neighbour)
            return ans
        dfs(self.kingName)
        return ans

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()