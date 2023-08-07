from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10**9 + 7

        nums = SortedList()
        
        # Total Cost to return
        totalCost = 0
        
        for element in instructions:
            
            n = len(nums)
            
            floorIdx = nums.bisect_left(element)

    
            ceilIdx = nums.bisect_right(element)

            totalCost += min(floorIdx, n - ceilIdx)

            totalCost %= mod
                
            nums.add(element)
			
        return totalCost