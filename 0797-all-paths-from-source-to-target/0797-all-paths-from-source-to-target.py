class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dicti=defaultdict(list)
        no_of_path=[]
        for fr in range(len(graph)):
            for to in range(len(graph[fr])):
                dicti[fr].append(graph[fr][to])
        
        path = [0]
        def dfs(vertex):

            if vertex == len(graph)-1:
                no_of_path.append(path[:])
                return
            for neighbour in dicti[vertex]:
                path.append(neighbour)
                dfs(neighbour)
                path.pop()                
        dfs(0)
        return no_of_path
       
        