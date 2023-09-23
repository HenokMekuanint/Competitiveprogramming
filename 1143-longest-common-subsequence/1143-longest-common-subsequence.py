class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for i in range(len(text2))] for i in range(len(text1))]
        @cache
        def dp(index1, index2):
            if index1 < 0 or index2 < 0:
                return 0
            if memo[index1][index2]!=-1:
                return memo[index1][index2]
            if text1[index1] == text2[index2]:
                memo[index1][index2]= 1 + dp(index1 - 1, index2 - 1)
            else:
                memo[index1][index2]= max(dp(index1 - 1, index2), dp(index1, index2 - 1))
            return memo[index1][index2]

        return dp(len(text1) - 1, len(text2) - 1)
                
        