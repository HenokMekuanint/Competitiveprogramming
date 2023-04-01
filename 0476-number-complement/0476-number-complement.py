class Solution:
    def findComplement(self, num: int) -> int:
        temp=['0','b']
        temp.extend(['1' if i=='0' else '0' for i in bin(num)[2:]])
        return int("".join(temp),2)
        