class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        
        while left<=right:
            mid=(left+right)//2
            cur_pro=mid*mid
            if cur_pro<x:
                left=mid+1
            elif cur_pro>x:
                right=mid-1
            else:
                return mid
        return right
        