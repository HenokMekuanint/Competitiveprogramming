class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window=defaultdict(int)
        compare=Counter(t)
        have=0
        need=len(compare)
        left=0
        length=float("inf")
        ans=""
        for right in range(len(s)):
            if s[right] in compare:
                window[s[right]]+=1
                if window[s[right]]==compare[s[right]]:
                    have+=1
            while have==need:
                if length>right-left+1:
                    ans=s[left:right+1]
                    length=right-left+1
                if s[left] in window and window[s[left]]==compare[s[left]]:
                    have-=1
                if s[left] in window:
                    window[s[left]]-=1
                left+=1
        return ans