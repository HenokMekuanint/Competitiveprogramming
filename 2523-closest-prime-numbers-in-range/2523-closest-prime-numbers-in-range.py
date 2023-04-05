class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans=float("inf")
        temp=[-1,-1]
        def prime_sieve(num):
            is_prime=[True for i in range(num+1)]
            i=2
            is_prime[0]=is_prime[1]=False
            while i*i<=num:
                if is_prime[i]:
                    j=i*i
                    while j<=num:
                        is_prime[j]=False
                        j+=i
                i+=1
            return [i for i in range(2, num + 1) if is_prime[i]]
        primes=prime_sieve(right)
        temp2=[]
        for i in range(len(primes)):
            if primes[i]>=left:
                temp2=primes[i:]
                break
        
        for i in range(1,len(temp2)):
            if ans>temp2[i]-temp2[i-1]:
                temp[0]=temp2[i-1]
                temp[1]=temp2[i]
                ans=temp2[i]-temp2[i-1]
        return temp
        
        
                    
        