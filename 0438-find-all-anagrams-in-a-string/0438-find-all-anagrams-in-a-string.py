class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # count=Counter(p)
        # ans=[]
        # for i in range(len(s)-len(p)+1):
        #     _dict=defaultdict(int)
        #     for j in range(i,i+len(p)):
        #         _dict[s[j]]+=1
        #     if count==_dict:
        #         ans.append(i)
        # return ans
        
        count=Counter(p)
        left=0
        ans=[]
        _dict=defaultdict(int)
        for right in range(len(s)):
            _dict[s[right]]+=1

            while right-left+1>len(p):
                _dict[s[left]]-=1
                if _dict[s[left]]==0:
                    del _dict[s[left]]
                left+=1

            if  count==_dict:
                ans.append(left)
        return ans