def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        newarray=[]
        for i in nums:
            newarray.append(int(i))
        newarray.sort()
        return str(newarray[-k])
