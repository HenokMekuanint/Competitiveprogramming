class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg=float("-inf")
        left=0
        cur_sum=0
        for right in range(len(nums)):
            cur_sum+=nums[right]
            while right-left+1>k:
                cur_sum-=nums[left]
                left+=1
            if right-left+1==k:
                max_avg=max(cur_sum/k,max_avg)
        return max_avg