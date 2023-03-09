class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def combination(temp,index):
            if len(temp)==k:
                res.append(temp)
                return
            else:
                for i in range(index,n+1):
                    combination(temp+[i], i+1)
              
        combination([],1)
        return res
            