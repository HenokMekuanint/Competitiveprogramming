class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        [8,1,2,2,3]
        [1,2,2,3,8]
        
        """
        dicti={}
        temp=sorted(nums)
        for i in range(len(temp)):
            if temp[i] in dicti:
                continue
            else:
                dicti[temp[i]]=i
        for i in range(len(nums)):
            temp[i]=dicti[nums[i]]
        return temp