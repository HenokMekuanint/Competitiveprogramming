class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        comb=[]
        dicti=defaultdict(int)
        def combination(temp,index):
            if temp:
                    comb.append(temp)
            if index==len(nums):
                return
            
            for i in range(index,len(nums)):
                
                combination([nums[i]]+temp,i+1)
        combination([],0)
        for i in range(len(comb)):
            var=0
            for j in range(len(comb[i])):
                var|=comb[i][j]
            dicti[i]=var
        max_or=max(dicti.values())
        ans=0
        for num in dicti.values():
            if num==max_or:
                ans+=1
        return ans
        