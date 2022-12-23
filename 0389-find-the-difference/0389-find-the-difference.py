class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=''.join(sorted(s))
        t=''.join(sorted(t))
        # if len(s)==0:return t
        pointer=0
        while pointer<len(s):
            if s[pointer]==t[pointer]:
                pointer+=1
            else:
                return t[pointer]
        return t[-1]
        