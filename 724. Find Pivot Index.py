class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        leftsum=0
        for i in range(len(nums)):
            rightsum=total-leftsum-nums[i]
            if rightsum==leftsum:
                return i
            else:
                leftsum+=nums[i]
        return -1
