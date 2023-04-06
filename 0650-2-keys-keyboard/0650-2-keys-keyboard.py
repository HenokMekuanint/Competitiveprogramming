class Solution:
    def minSteps(self, n: int) -> int:
        i=2
        primes=[]
        while i*i<=n:
            while n%i==0:
                
                primes.append(i)
                n//=i
            i+=1
        if n>1:
            primes.append(n)
        return sum(primes)
        