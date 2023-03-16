class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def combination(temp,index):
            if sum(temp)>target:
                return
            if sum(temp)==target:
                ans.append(temp)
            for i in range(index,len(candidates)):
                combination(temp+[candidates[i]],i)
        combination([],0)
        return ans
                