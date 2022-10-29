class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         [2,3,1,2,4,3]
#              L
#                    R
        if target > sum(nums): return 0
        left=0
        sumission=0
        minlen=float('inf')
        for right in range(len(nums)):
            sumission+=nums[right]
            while sumission>=target:
                minlen=min(right-left+1,minlen)
                sumission-=nums[left]
                left+=1
            
        return minlen
