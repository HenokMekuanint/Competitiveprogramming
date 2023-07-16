class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        max_length = 0

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                max_length = max(max_length, dp[i][diff])

        return max_length

                