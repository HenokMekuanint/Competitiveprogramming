class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        def backtrack(temp,index):
            if len(temp)>=4 and index<len(s)-1:
                return
            if len(temp)==4 and index==len(s):
                ans.append(".".join(temp))
            for i in range(index,len(s)):
                if int(s[index:i+1])>255 or (len(s[index:i+1])>1 and s[index]=="0"):
                    continue
                backtrack(temp+[s[index:i+1]],i+1)
        backtrack([],0)
        return ans
        