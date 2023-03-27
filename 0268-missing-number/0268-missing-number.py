class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        end=max(nums)
        temp=[0 for i in range(len(nums)+1)]
        for num in nums:
            temp[num]+=1
        
        for i in range(len(temp)):
            if temp[i]==0:
                return i
            else:
                continue
            
            
        