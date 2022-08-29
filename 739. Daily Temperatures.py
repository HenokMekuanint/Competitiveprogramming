class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stack=[]
        array=[0 for i in range(len(nums))]

        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                poppedindex=stack.pop()
                array[poppedindex]=i-poppedindex
            else:
                stack.append(i)
        return array
