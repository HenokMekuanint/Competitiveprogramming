class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def combination(temp,index):
            if index==len(nums):
                ans.append(temp)
                return
            
            for i in range(index,len(nums)):
                if temp not in ans:
                    ans.append(temp)
                combination(temp+[nums[i]],i+1)
        combination([],0)
        return ans