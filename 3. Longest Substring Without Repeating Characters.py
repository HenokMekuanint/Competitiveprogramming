class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
    
        max_len = 0

        for i in range(len(s)):
            _map = {}
            _map[s[i]] = 1

            for j in range(i+1, len(s)):
                temp = j
                if s[j] not in _map:
                    _map[s[j]] = 1
                else:
                    break

            max_len = max(max_len, len(_map))

        return max_len
