class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        values=list(dict.values())
        keys=list(dict.keys())
        maximum=keys[values.index(max(values))]
        return maximum
