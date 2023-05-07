class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dicti=defaultdict(int)
        for word in words:
            dicti[word]+=1
        dicti=dict(sorted(dicti.items(),key=lambda x:x[1],reverse=True))
        ans=[]
        comp=list(dicti.values())[:k]
        comp=set(comp)
        for key in dicti:
            if dicti[key] in comp:
                ans.append((key,dicti[key]))
        ans_dicti2=defaultdict(list)
        for stri,index in ans:
            ans_dicti2[index].append(stri)
        
        for key in ans_dicti2:
            ans_dicti2[key]=sorted(ans_dicti2[key])
        rtn=[]
        for key in ans_dicti2:
            for word in ans_dicti2[key]:
                rtn.append(word)
                if len(rtn)==k:
                    return rtn
        return rtn
        
            
            
        