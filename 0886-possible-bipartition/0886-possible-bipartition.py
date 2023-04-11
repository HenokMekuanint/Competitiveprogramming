class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dicti=defaultdict(list)
        for neigh1,neigh2 in dislikes:
            dicti[neigh1].append(neigh2)
            dicti[neigh2].append(neigh1)
        set1=set()
        set2=set()
        visited=set()
        ans=[True]
        def dfs(vertex,flag):
            if vertex  in visited:
                if (flag==False and vertex in set1) or (flag==True and vertex in set2):
                    ans[0]=False
                return
            else:
                if flag==True:
                    set1.add(vertex)
                else:
                    set2.add(vertex)
                visited.add(vertex)
            for neighbour in dicti[vertex]:
                dfs(neighbour,not flag)
        for key in dicti:
            if key not in visited:
                dfs(key,True)
        return ans[0]
                
                
                    
                    
                
            
            
        
        
        
        