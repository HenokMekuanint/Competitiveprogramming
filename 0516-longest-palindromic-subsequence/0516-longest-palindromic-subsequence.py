class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        dp[0][0] = 1
        ans = 0
        
        for i in range(n):
            for j in range(1, n  - i + 1):
                if i == 0:
                    dp[j][j + i] = 1
                elif s[j - 1] == s[i + j - 1]:
                    dp[j][j + i] = max(dp[j + 1][j + i - 1] + 2, dp[j][j + i])
                else:
                    dp[j][j + i] = max(dp[j + 1][i + j], dp[j][i + j - 1])
                ans = max(ans, dp[j][j + i])
            
        
        return ans
        