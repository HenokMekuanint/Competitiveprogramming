class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        MOD = 10 ** 9 + 7
        N = len(nums)
        freqs = [0 for _ in range(N + 1)]
        for s, e in requests:
            freqs[s] += 1
            freqs[e + 1] -= 1
            
        for i in range(1, N + 1):
            freqs[i] += freqs[i - 1]
        freqs.pop()
        ans = 0
        for n, f in zip(sorted(nums), sorted(freqs)):
            ans += n * f
        return ans % MOD
        
        
        