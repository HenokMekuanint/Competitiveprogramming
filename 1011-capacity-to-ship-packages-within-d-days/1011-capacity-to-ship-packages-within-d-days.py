class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        def canship(m):
            req_days=1
            cur_cap=m
            for w in weights:
                if cur_cap-w<0:
                    req_days+=1
                    cur_cap=m
                cur_cap-=w
            return req_days<=days
        while l<=r:
            m=(l+r)//2
            if canship(m):
                res=min(m,res)
                r=m-1
            else:
                l=m+1
        return res
                
            
        