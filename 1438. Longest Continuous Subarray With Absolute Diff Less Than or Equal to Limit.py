from collections import deque
class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        hi = deque()
        lo = deque()
        ans = 0
        i = 0
        for j in range(len(nums)):
            while hi and nums[hi[-1]] <= nums[j]:
                hi.pop()
            while lo and nums[lo[-1]] >= nums[j]:
                lo.pop()
            hi.append(j)
            lo.append(j)
            if len(hi) == 1:   
                while nums[hi[0]] - nums[lo[0]] > limit:
                    ans = max(ans, j - i)
                    i = lo.popleft() + 1
            elif len(lo) == 1:
                while nums[hi[0]] - nums[lo[0]] > limit:
                    ans = max(ans, j - i)
                    i = hi.popleft() + 1
        return max(ans, j - i + 1)
