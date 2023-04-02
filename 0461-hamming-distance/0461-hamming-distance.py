class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        temp=x^y
        while temp>0:
            if temp &1:
                count+=1
            temp=temp>>1
        return count
        