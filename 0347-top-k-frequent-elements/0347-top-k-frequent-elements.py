class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp=[]
        dicti=defaultdict(int)
        for num in nums:
            dicti[num]+=1
        dicti=dict(sorted(dicti.items(),key=lambda x:x[1],reverse=True))
        for num in dicti:
            temp.append(num)
            if k==1:
                break
            k-=1
        return temp
            
            
       
        