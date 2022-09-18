class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        values=list(dict.values())
        for i in range(len(values)):
            if  values[i]!=1:
                return True
        return False
