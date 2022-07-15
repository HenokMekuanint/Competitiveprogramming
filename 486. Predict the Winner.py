class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        if len(nums) <= 2:
            return True
        pre = list(nums)
        cur = list(nums)
        for size in range(1, len(pre)):
            for i in range(len(pre) - size):
                j = i + size
                cur[j] = max(nums[i] - pre[j], nums[j] - pre[j - 1])
            pre = list(cur)

        # print(cur)
        return cur[-1] >= 0
