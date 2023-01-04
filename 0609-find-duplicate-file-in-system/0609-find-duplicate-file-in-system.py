class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dicti=defaultdict(list)
        ans=[]
        for i in range(len(paths)):
            path=paths[i]
            path=list(path.split())
            path[0]+="/"
            for j in range(1,len(path)):
                temp=path[j].split("(")
                temp[1]=temp[1][:-1]
                dicti[temp[1]].append(path[0]+temp[0])
        for value in dicti.values():
            if len(value)>1:ans.append(value)
        return ans
                