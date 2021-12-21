 def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=0
        newarray=[]
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i!=j and nums[i]>nums[j]:
                    count+=1
            newarray.append(count)
            count=0
        return newarray
