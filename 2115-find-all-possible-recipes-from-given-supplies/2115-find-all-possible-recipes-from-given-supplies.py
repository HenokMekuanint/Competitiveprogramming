class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph=defaultdict(list)
        dependency=defaultdict(int)
        ans=[]
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
            dependency[recipes[i]]=len(ingredients[i])
        def bfs(nodes):
            queue=deque(nodes)
            while queue:
                node=queue.popleft()
                for neighbour in graph[node]:
                    dependency[neighbour]-=1
                    if not dependency[neighbour]:
                        queue.append(neighbour)
                        ans.append(neighbour)
            return ans
        return bfs(supplies)
                    
        