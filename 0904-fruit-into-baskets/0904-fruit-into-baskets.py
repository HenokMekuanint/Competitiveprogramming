class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dicti=defaultdict(int)
        left=0
        ans=0
        for right in range(len(fruits)):
            dicti[fruits[right]]+=1
            while left<right and len(dicti)>2:
                dicti[fruits[left]]-=1
                if dicti[fruits[left]]==0:
                    del dicti[fruits[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans
            
        