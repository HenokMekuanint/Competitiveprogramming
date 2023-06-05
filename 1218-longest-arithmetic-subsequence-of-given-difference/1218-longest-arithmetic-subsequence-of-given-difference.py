class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo=defaultdict(int)
        longest=1
        for i in range(len(arr)-1,-1,-1):
            current=1+memo[arr[i]+difference]
            memo[arr[i]]=current
            longest=max(longest,current)
        return longest