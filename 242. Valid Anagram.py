class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for i in s:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for i in t:
            if i in dict2:
                dict2[i]+=1
            else:
                dict2[i]=1
                
        answer=True
        for i in dict1:
            if i not in dict2 or dict2[i]!=dict1[i]:
                answer=False
        for i in dict2:
            if i not in dict1 or dict2[i]!=dict1[i]:
                answer=False
        return answer
