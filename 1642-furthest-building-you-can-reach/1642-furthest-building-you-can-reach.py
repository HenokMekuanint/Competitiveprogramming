class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladderSizes = [0] * ladders
        heapq.heapify(ladderSizes)
        i = 0
        while i < len(heights) - 1:
            h = heights[i+1] - heights[i]
            if h <= 0:
                i += 1
            else:
                if ladders == 0 or h < ladderSizes[0]:
                    if h <= bricks:
                        bricks -= h
                        i += 1
                    else:
                        break
                else:

                    if bricks >= ladderSizes[0]:
                        bricks -= ladderSizes[0]
                        heapq.heappushpop(ladderSizes, h)
                        i += 1
                    else:
                        break
                        
        return i