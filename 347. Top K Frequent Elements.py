class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums=sorted(nums)
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        newlist=[]
        for i in range(0,k):
            listofvalues = list(dict.values())
            listofkeys = list(dict.keys())
            listofvalues=sorted(listofvalues)
            keys = [k for k, v in dict.items() if v == listofvalues[-1]]

            if keys:
                newlist.append(keys[0])
                dict.pop(keys[0])
                keys=[]
        return newlist
