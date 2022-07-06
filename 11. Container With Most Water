class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maximumArea = ((j - i) * min(height[i], height[j]) )
        while i < j:
            if height[i] < height [j]:
                i += 1
    
            else:
                j -= 1
            maximumArea = max(maximumArea,((j - i) * min(height[i], height[j]) ) )

        return maximumArea
