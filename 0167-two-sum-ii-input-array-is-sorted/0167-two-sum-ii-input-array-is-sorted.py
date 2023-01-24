class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        while left<right:
            cur_sum=nums[left]+nums[right]
            if cur_sum>target:
                right-=1
            elif cur_sum<target:
                left+=1
            else:
                return [left+1,right+1]