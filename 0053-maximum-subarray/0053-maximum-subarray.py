class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left=0
        right=0
        total=float("-inf")
        cur_sum=0
        while right<len(nums):
            cur_sum+=nums[right]
            total=max(total,cur_sum)
            if cur_sum>=0:
                right+=1
            elif cur_sum<0:
                cur_sum=0
                right=right+1
        return total
            