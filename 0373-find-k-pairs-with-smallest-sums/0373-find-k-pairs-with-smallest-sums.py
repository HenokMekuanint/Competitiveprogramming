class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        if not nums1 or not nums2:
            return []

        # Create a min heap to store pairs (sum, i, j)
        # where sum = nums1[i] + nums2[j]
        heap = [(nums1[0] + nums2[0], 0, 0)]

        # Keep track of pairs that have been explored
        explored = set((0, 0))

        # Keep adding pairs to the result until k pairs have been found
        result = []
        while len(result) < k and heap:
            # Pop the smallest pair from the heap
            _, i, j = heapq.heappop(heap)

            # Add the pair to the result
            result.append([nums1[i], nums2[j]])

            # Check if there are any new pairs to be added to the heap
            if i+1 < len(nums1) and (i+1, j) not in explored:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
                explored.add((i+1, j))
            if j+1 < len(nums2) and (i, j+1) not in explored:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
                explored.add((i, j+1))

        return result
        