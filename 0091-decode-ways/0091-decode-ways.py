class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        memo={}
        def dp(index,temp):
            
            if index==len(s):
                return 1
            if index>len(s):
                return 0
            if s[index]=="0":
                return 0
            if index in memo:
                return memo[index]
            hold=""
            ans=0
            for i in range(index,index+2):
                if i<len(s):
                    hold+=s[i]
                if int(hold)<27:
                    ans+=dp(i+1,temp+hold)
            memo[index]=ans
            return memo[index]
        return dp(0,"")
                
        