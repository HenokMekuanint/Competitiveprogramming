class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        array=[-1 for i in range(len(nums))]
        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                poppedindex=stack.pop()
                array[poppedindex]=nums[i]
            else:
                stack.append(i)
        
        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                poppedindex=stack.pop()
                array[poppedindex]=nums[i]
            else:
                stack.append(i)
        return array
