class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans=[]
        s=s.split()
        max_iter=index=0
        for w in range(len(s)):
            if max_iter<=len(s[w]):
                index=w
                max_iter=len(s[w])
                k=len(s[index])-1
        for i in range(max_iter):
            temp=""
            space=""
            for j in range(len(s)):
                if i >=len(s[j]):
                    space+=" "
                else:
                    temp+=space
                    temp+=s[j][i]
                    space=""
            ans.append(temp)
        return ans
        