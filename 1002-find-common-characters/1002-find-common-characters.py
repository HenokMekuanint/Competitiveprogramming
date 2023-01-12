class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        words=["bella","label","roller"]
        word="bella"
        i=0
        dict={
        b:[[0,1]],
        e:[[0,1]],
        l:[[0,2],[1,l]]
        a:[[0,1]]
        }
        """
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
            
                
                
            
            
        