class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dicti=defaultdict(int)
        
        for num in nums:
            dicti[num]+=1
        for i in range(1,len(nums)+1):
            if dicti[i]>1:
                repeated=i
            if dicti[i]==0:
                miss=i
        return [repeated,miss]
        
                
        
        
        