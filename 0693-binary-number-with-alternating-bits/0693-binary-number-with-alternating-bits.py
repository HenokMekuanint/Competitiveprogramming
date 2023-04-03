class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp=n>>1
        temp=temp^n
        temp2=list(bin(temp)[2:])
        if 2**len(temp2)-1==temp:
            return True
        else:
            return False
         
        
        