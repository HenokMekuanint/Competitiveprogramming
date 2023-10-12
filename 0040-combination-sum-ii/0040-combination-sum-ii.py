class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        memo = {}

        def combination(temp, cur_sum, index):
            if cur_sum > target:
                return
            if cur_sum == target:
                ans.append(temp[:])  # Append a copy of 'temp'
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates
                combination(temp + [candidates[i]], cur_sum + candidates[i], i + 1)

        combination([], 0, 0)
        return ans