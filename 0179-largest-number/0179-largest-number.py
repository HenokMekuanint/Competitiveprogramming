class Solution:
   def largestNumber(self, nums: List[int]) -> str:
    
    
    if not any(map(bool,nums)):
        return '0'
    for i in range(len(nums)):
        nums[i]=str(nums[i])
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]>nums[j]+nums[i]:
                continue
            elif nums[i]+nums[j]<nums[j]+nums[i]:
                nums[i],nums[j]=nums[j],nums[i]
    return ("").join(nums)