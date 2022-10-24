class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        const=[0 for i in range(0,26)]
        var=[0 for i in range(0,26)]
        ans=[]
        for i in p:
            index=ord(i)-97
            const[index]+=1
        left=0
        for right in range(len(s)):
            while right-left+1>len(p):
                remindex=ord(s[left])-97
                var[remindex]-=1
                left+=1
            var[ord(s[right])-97]+=1
            if var==const:
                ans.append(left)
        return ans
