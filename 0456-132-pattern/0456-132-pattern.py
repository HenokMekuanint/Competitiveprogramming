class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack=[]
        cur_min=nums[0]
        for i in range(len(nums)):
            while stack and stack[-1][0]<=nums[i]:
                stack.pop()
            if stack and nums[i]<stack[-1][0] and nums[i]>stack[-1][1]:
                return True
            stack.append((nums[i],cur_min))
            cur_min=min(cur_min,nums[i])
        
        return False

