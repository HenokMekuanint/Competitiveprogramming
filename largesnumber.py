class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp1=str(nums[i])+str(nums[j])
                temp2=str(nums[j])+str(nums[i])
                if temp2>temp1:
                    nums[i],nums[j]=nums[j],nums[i]
        largestnumber=""
        zero=False
        for i in nums:
            if i!=0:
                zero=True
        if zero==False:
            largestnumber="0"
        else:
            for i in range(0,len(nums)):
                largestnumber+=str(nums[i])
        return largestnumber
        
