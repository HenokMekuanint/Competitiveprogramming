class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s = "AABABBA", k = 2
        #      L
        #         R
        #     windowlen=r-l+1
        #         {
        #             A:3
        #             B:1
        #         }
        #         3-2<=2
        
            left=0
            dicti=defaultdict(int)
            ans=0
            for right in range(len(s)):
                dicti[s[right]]+=1
                while (right-left+1)-max(dicti.values())>k:
                    dicti[s[left]]-=1
                    left+=1
                ans=max(ans,right-left+1)
            return ans
                


            
  