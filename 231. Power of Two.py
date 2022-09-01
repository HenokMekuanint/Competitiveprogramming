class Solution:
    def isPowerOfTwo(self, num: int) -> bool:
        
        if num==1:
            return True
        rem=num%2
        if rem!=0 or num==0:
            return False
        else:
            return self.isPowerOfTwo(num//2)
