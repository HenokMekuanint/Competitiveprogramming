class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        def prime_factor(pro):
            n=2
            prime=set()
            while n*n<=pro:
                while pro%n==0:
                    pro//=n
                    prime.add(n)
                n+=1
            if pro>1:
                prime.add(pro)
            return prime
        ans=set()
        for num in nums:
            ans=ans.union(prime_factor(num))
        return len(ans)
        