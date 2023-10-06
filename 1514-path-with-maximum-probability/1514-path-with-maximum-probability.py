class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        import heapq
        graph=defaultdict(list)
        for i in range(len(edges)):
            frm,to,prob=edges[i][0],edges[i][1],succProb[i]
            graph[frm].append((to,prob))
            graph[to].append((frm,prob))
        def djkstra(start):
            nonlocal n
            probability={i:float("-inf") for i in range(n)}
            probability[start]=0
            priority_queue=[(-1,start)]
            
            visited=set()
            while priority_queue:
                cur_prob,cur_node=heapq.heappop(priority_queue)
                cur_prob*=-1
                if cur_node in visited:
                    continue
                visited.add(cur_node)
                for neighbour,neigh_prob in graph[cur_node]:
                    prob=cur_prob*neigh_prob
                    if prob>probability[neighbour]:
                        probability[neighbour]=prob
                        heapq.heappush(priority_queue,(-1*prob,neighbour))
            return probability
        temp=djkstra(start_node)[end_node]
        
        return 0 if temp==float("-inf") else temp
        
                        