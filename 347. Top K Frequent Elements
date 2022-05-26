class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = {k:v for k, v in sorted(count.items(), key = lambda v: v[1], reverse = True )}
        iter = 0
        ans = []
        for i in count:
            if iter == k:
                break
            ans.append(i)
            iter += 1
        return ans
