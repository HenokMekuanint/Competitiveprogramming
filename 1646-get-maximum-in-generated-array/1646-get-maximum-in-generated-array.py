class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n<2:
            return n
            
        ans=[0,1]
        
        for i in range(n-1):
            if (i+2)%2==0:
                ans.append(ans[(i+2)//2])
            else:
                ans.append(ans[(i+2)//2]+ans[(i+2)//2+1])
        return max(ans)
            
        