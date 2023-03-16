class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def combination(temp,index):
            if sum(temp)>n:
                return
            if sum(temp)==n and len(temp)==k:
                ans.append(temp)
                return
            for i in range(index,9+1):
                combination(temp+[i],i+1)
        combination([],1)
        return ans
        