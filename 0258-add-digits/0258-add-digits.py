class Solution:
    def addDigits(self, num: int) -> int:
        
        while num>9:
            temp=str(num)
            num=0
            for i in range(len(temp)):
                num+=int(temp[i])
        return num
                
        