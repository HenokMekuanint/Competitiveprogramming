class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicti=Counter(s1)
        left=0
        dicti2=defaultdict(int)
        for right in range(len(s2)):
            dicti2[s2[right]]+=1
            if right-left+1>len(s1):
                dicti2[s2[left]]-=1
                if dicti2[s2[left]]==0:
                    del dicti2[s2[left]]
                left+=1
            if dicti2==dicti:
                return True
        return False
            
            