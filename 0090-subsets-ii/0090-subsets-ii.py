class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def combination(temp,index):
            if index==len(nums):
                ans.append(temp)
                return
            
            for i in range(index,len(nums)):
                if temp not in ans:
                    ans.append(temp)
                combination(temp+[i],i+1)
        combination([],0)
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                ans[i][j]=nums[ans[i][j]]
        
        return list(set(tuple(sorted(sub)) for sub in ans))