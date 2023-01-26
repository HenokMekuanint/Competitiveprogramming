class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans=[]
        dicti=defaultdict(int)
        for i in range(len(s)):
            dicti[s[i]]=i
        end=0
        counter=1
        for i in range(len(s)):
            if dicti[s[i]]>end:
                end=dicti[s[i]]
            if i==end:
                ans.append(counter)
                end=0
                counter=0
            counter+=1
        return ans