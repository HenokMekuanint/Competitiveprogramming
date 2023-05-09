class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        max_heap=[-pile for pile in piles]
        heapq.heapify(max_heap)
        while k:
            top=-1*heapq.heappop(max_heap)
            top=math.ceil(top/2)
            heapq.heappush(max_heap,-1*top)
            k-=1
        return -1*sum(max_heap)
            
        
        