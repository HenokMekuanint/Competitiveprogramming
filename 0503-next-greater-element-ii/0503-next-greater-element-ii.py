class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[-1 for i in range(len(nums))]
        stack=[]
        size=len(nums)
        for  i in range(2*size):
            while stack and nums[stack[-1]]<nums[i%size]:
                poppedindex=stack.pop()
                ans[poppedindex]=nums[i%size]
            stack.append(i%size)
        return ans