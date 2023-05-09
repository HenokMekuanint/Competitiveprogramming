class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        min_heap = []
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                num = matrix[i][j]
                if len(min_heap) < k:
                    heapq.heappush(min_heap, -num)
                else:
                    if num < -min_heap[0]:
                        heapq.heappop(min_heap)
                        heapq.heappush(min_heap, -num)

        return -min_heap[0]
        