class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        freq = {}
        need = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in nums:
            if freq[num] == 0:
                continue

            freq[num] -= 1

            if need.get(num-1, 0) > 0:
                need[num-1] -= 1
                need[num] = need.get(num, 0) + 1
            elif freq.get(num+1, 0) > 0 and freq.get(num+2, 0) > 0:
                freq[num+1] -= 1
                freq[num+2] -= 1
                need[num+2] = need.get(num+2, 0) + 1
            else:
                return False

        return True