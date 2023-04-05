class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dicti=defaultdict(int)
        for num in deck:
            dicti[num]+=1
        def prime_fact(num):
            n=2
            primes=set()
            while n*n<=num:
                while num%n==0:
                    num//=n
                    primes.add(n)
                n+=1
            if num>1:
                primes.add(num)
            return primes
        temp=sorted(list(dicti.values()))
        prime_min=list(prime_fact(min(temp)))
        print(prime_min)
        for i in range(len(prime_min)):
            for j in range(len(temp)):
                if temp[j]%prime_min[i]!=0:
                    break
                if temp[j]%prime_min[i]==0 and j==len(temp)-1:
                    return True
        
        
        return False
                
            
            
            
            
        