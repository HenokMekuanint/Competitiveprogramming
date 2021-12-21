def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        newarray=[]
        for i in range(0,len(nums)):
            if nums[i]==target:
                newarray.append(i)
        return newarray
