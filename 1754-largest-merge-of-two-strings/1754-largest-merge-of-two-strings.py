class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        lword1=list(word1)
        lword2=list(word2)
        ans=""
        while lword1 and lword2:
            if "".join(lword1)>"".join(lword2):
                ans+=lword1.pop(0)
            elif "".join(lword1)<"".join(word2):
                ans+=lword2.pop(0)
            else:
                while  "".join(lword1)=="".join(word2) and len(lword1)>1 and len(lword2)>1:
                    if "".join(lword1)=="".join(word2):
                        ans+=lword1.pop(0)
                    elif "".join(lword1)>"".join(lword2):
                        ans+=lword1.pop(0)
                    elif "".join(lword1)<"".join(word2):
                        ans+=lword2.pop(0)
                    
        if lword1:
            ans+="".join(lword1)
        if lword2:
            ans+="".join(lword2)
        return ans