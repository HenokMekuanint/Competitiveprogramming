class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_range(start, end):
            prev_max = 0
            curr_max = 0

            for i in range(start, end):
                temp = curr_max
                curr_max = max(prev_max + nums[i], curr_max)
                prev_max = temp

            return curr_max

        n = len(nums)
        if n == 1:
            return nums[0]
        return max(rob_range(0, n - 1), rob_range(1, n))