class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        dicti=defaultdict(list)
        for i in range(1,len(parent)):
            dicti[parent[i]].append(i)
        ans=1
        def dfs(vertex):
            nonlocal ans
            if  not dicti[vertex]:
                return s[vertex]
            temp=[]
            
            for neighbour in dicti[vertex]:
                var=dfs(neighbour)
                if s[vertex]!=var[-1]:
                    if len(temp)<2:
                        temp.append(var)
                    elif len(temp)==2:
                        if len(var)>len(temp[0]):
                            temp[0]=var
                    temp=sorted(temp,key=lambda x:len(x))
            if not temp:
                return s[vertex]
            if len(temp)==1:
                ans=max(ans,len(temp[0])+1)
                return temp[0]+s[vertex]
            ans=max(ans,len(temp[-1])+len(temp[-2])+1)
            return temp[-1]+s[vertex]
        dfs(0)
        return ans
            
                    
            
            
                
        