class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c==0:return True
        import math
        n=math.floor(math.sqrt(c))+1
        for b in range(1,n):
            a=math.sqrt(c-(b**2))
            if float(a).is_integer():
                return True
        return False
                
        