class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        nums.sort()
        
        max_gap=0
        for i in range(1,len(nums)):
            diff=abs(nums[i]-nums[i-1])
            if diff>max_gap:
                max_gap=diff
                
        return max_gap
