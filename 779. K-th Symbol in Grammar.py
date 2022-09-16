class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N==1: return 0
        parent=self.kthGrammar(N-1,K//2+K%2)
        iskOdd=K%2==1
        if parent==1:
            return 1 if iskOdd else 0
        else:
            return 0 if iskOdd else 1
        
