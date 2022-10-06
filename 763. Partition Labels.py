class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex={}
        for i in range(len(s)):
            lastindex[s[i]]=i
        end=0
        size=0
        array=[]
        for i in range(len(s)):
            size+=1
            end=max(end,lastindex[s[i]])
            if i==end:
                array.append(size)
                size=0
        return array
