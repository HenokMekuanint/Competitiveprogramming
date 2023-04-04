class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        def GCD(a,b):
            if b==0:
                return a
            return GCD(b,a%b)
        gcd=GCD(nums[0],nums[-1])
        return gcd
            
            
        