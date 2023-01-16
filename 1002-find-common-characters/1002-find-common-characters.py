class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(97,124):
            char=chr(i)
            fre=0
            temp=[]
            for word in words:
                fre=word.count(char)
                temp.append(fre)
            ans.extend([char]*min(temp))
        return ans
            
                
            
            
        