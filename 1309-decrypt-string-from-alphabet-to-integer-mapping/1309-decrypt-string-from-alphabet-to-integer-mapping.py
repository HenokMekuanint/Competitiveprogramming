class Solution:
    def freqAlphabets(self, s: str) -> str:
        _dict=defaultdict(str)
        ans=""
        for _ord in range(97,123):
            if _ord<=105:
                _dict[str(_ord-96)]=chr(_ord)
                
            else:
                _dict[str(_ord-96)+"#"]=chr(_ord)
                
        stack=[]
        for r in range(len(s)):
            if s[r]!="#" and len(stack)<2:
                stack.append(s[r])
                
            elif s[r]=="#" and len(stack)==2:
                ans+=(_dict[stack.pop(0)+stack.pop(0)+s[r]])
                
            elif len(stack)==2:
                ans+=(_dict[stack.pop(0)])
                stack.append(s[r])
                
        if stack: 
            for i in stack:
                ans+=_dict[i]
        return ans
                
            
        