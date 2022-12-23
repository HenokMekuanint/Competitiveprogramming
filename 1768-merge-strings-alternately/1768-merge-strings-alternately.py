class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer,ans=0,""
        while pointer<min(len(word1),len(word2)):
            ans+=word1[pointer]
            ans+=word2[pointer]
            pointer+=1
        if len(word1)>len(word2):
            ans+=word1[pointer:]
        elif len(word1)<len(word2):
            ans+=word2[pointer:]
        return ans
        