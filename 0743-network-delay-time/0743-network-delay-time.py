class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        graph=defaultdict(list)
        for frm,to,weight in times:
            graph[frm].append((to,weight))
        def dkstra(start):
            distances={i:float("inf") for i in range(1,n+1)}
            distances[start]=0
            visited=set()
            priority_queue=[(0,start)]
            while priority_queue:
                current_distance,current_node=heapq.heappop(priority_queue)
                if current_node in visited:
                    continue
                visited.add(current_node)
                for neighbour,weight in graph[current_node]:
                    distance=current_distance+weight
                    if distance<distances[neighbour]:
                        distances[neighbour]=distance
                        heapq.heappush(priority_queue,(distance,neighbour))
            return distances
        temp=dkstra(k)
        ans=float("-inf")
        for key in temp:
            if temp[key]==float("inf"):
                return -1
            ans=max(ans,temp[key])
        return ans
                
            
            
            
        
            
            
        