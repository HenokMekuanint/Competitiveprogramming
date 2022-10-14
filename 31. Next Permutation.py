class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        lastpicindex=-1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                lastpicindex=i
        if lastpicindex==-1:
            for i in range(len(nums)//2):
                nums[i],nums[len(nums)-1-i]=nums[len(nums)-1-i],nums[i]
            return 
        index=lastpicindex
        for i in range(lastpicindex+1,len(nums)):
            if nums[i]>nums[lastpicindex-1] and nums[i]<nums[index]:
                index=i
        nums[lastpicindex-1],nums[index]=nums[index],nums[lastpicindex-1]
        nums[lastpicindex:]=sorted(nums[lastpicindex:])
        return 
