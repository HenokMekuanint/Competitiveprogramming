class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans=[0 for i in range(n+1)]
        for num in range(1,n+1):
            index=num
            while num>0:
                if num & 1:
                    ans[index]+=1
                num=num>>1
        return ans
            
            
            
        
        