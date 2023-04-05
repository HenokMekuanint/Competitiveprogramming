class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans=0
        temp=[]
        for word in words:
            shift=0
            num=0
            for i in range(len(word)):
                t=ord(word[i])-ord("a")
                shift=1<<t
                num=num|shift
            temp.append(num)
        for i in range(len(temp)):
            for j in range(i+1,len(temp)):
                if temp[i]&temp[j]==0:
                    ans=max(ans,len(words[i])*len(words[j]))
        return ans
                
                
            
                
        