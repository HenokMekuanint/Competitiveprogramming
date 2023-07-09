class Solution:
    def reversePairs(self, a: List[int]) -> int:
        ans=0
        def merge(s):
            nonlocal ans
            o=len(s)
            if o==1:
                return s
            m=o//2
            x=merge(s[:m])
            y=merge(s[m:])
            b=len(x)
            for i in y:
                ans+=b-bisect_right(x,2*i)
            return sorted(x+y)
        merge(a)
        return ans