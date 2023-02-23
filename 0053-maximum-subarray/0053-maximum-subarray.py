class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        running_sum = 0
        for num in nums:
            running_sum = max(running_sum + num, num)
            ans = max(ans, running_sum)
        return ans
