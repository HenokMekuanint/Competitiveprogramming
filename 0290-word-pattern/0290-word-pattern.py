class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=s.split()
    
        if len(pattern)!=len(a):
            
            return False
        dicti={}
        has_key=defaultdict(int)
        for i in range(len(pattern)):
            if pattern[i] in dicti:
                if dicti[pattern[i]]!=a[i]:
                    
                    return False
            else:
                if  has_key[a[i]]:
                    return False
                dicti[pattern[i]]=a[i]
                has_key[a[i]]=1
        return True