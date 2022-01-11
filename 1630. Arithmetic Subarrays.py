class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        array=[]
        for i in range(0,len(l)):
            newnums=nums[l[i]:r[i]]
            newnums.append(nums[r[i]])
            newnums.sort()
            result = [b - a for a,b in zip(newnums[:-1], newnums[1:])]
            s3=set(result)
            if len(s3)==1:
                array.append(True)
            else:
                array.append(False)
        return array
