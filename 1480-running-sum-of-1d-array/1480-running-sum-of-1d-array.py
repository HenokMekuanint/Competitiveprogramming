class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=0
        ans=[]
        for i in range(len(nums)):
            total+=nums[i]
            ans.append(total)
        return ans
            