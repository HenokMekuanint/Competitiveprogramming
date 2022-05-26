class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        rounds = len (nums)
        if (len(nums) % 2 ) == 0:
            rounds = (len(nums) // 2)

        for i in range( rounds):
            ans.append(nums[i])
            if nums [i] == nums[0-(i+1)]:
                break
            ans.append(nums[0-(i+1)])
        return ans
