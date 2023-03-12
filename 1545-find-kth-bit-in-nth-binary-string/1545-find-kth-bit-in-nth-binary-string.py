class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rev(s):
            return "".join(reversed(list(s)))
        def inv(s):
            return "".join(["0" if num=="1" else "1" for num in s])
        
        def findk(s,n):
            if n==1:
                return s[k-1]
            else:
                return findk(s+"1"+rev(inv(s)),n-1)
        return findk("0",n)
            
        