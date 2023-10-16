class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        for i in range(len(equations)):
            frm=equations[i][0]
            to=equations[i][1]
            weight=values[i]
            graph[frm].append((to,weight))
            graph[to].append((frm,1/weight))
        def dfs(node,res,visited):
            nonlocal dest
            if node==dest:
                return float(res)
            
            
            for neighbour,weight in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    temp=dfs(neighbour,res*weight,visited)
                    visited.remove(neighbour)
                    if temp!=None:
                        return temp
            return 
        ans=[]
        for frm,to in queries:
            if frm not in graph or to not in graph:
                ans.append(-1.0)
            elif frm==to:
                ans.append(1.0)
            else:
                dest=to
                rtn=dfs(frm,1,set([frm]))
                if rtn==None:
                    ans.append(-1.0)
                else:
                
                    ans.append(rtn)
        return ans
                
            