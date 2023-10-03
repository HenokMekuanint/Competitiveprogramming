class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=s.split()
    
        if len(pattern)!=len(a):
            
            return False
        dicti={}
        for i in range(len(pattern)):
            if pattern[i] in dicti:
                if dicti[pattern[i]]!=a[i]:
                    
                    return False
            else:
                if a[i] in dicti.values():
                    return False
                dicti[pattern[i]]=a[i]
        return True