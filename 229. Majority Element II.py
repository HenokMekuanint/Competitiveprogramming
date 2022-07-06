class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import math

        occurrence=math.floor(len(nums)/3)
        dict={}
        for i in nums:
            if (i in dict):
                dict[i] += 1
            else:
                dict[i]=1
        newarray=[]
        for i in dict.keys():
            if dict[i]>occurrence:
                newarray.append(i)
        return newarray
        
