class Solution:
    def isHappy(self, n: int) -> bool:

        while n>9:
            temp=0
            for i in str(n):
                temp+=(int(i)**2)
            n=temp
       
        return n==1 or n==7
        