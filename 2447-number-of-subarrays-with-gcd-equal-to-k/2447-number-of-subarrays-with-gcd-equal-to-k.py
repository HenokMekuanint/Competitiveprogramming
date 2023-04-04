class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def GCD(a,b):
            if b==0:
                return a
            return GCD(b,a%b)
        res=0
        for i in range(len(nums)):
            cur_gcd=0
            for j in range(i,len(nums)):
                cur_gcd=GCD(cur_gcd,nums[j])
                if cur_gcd==k:
                    res+=1
                elif cur_gcd<k:
                    break
        return res
            
                        
                        
                    
            
        
            
        
        