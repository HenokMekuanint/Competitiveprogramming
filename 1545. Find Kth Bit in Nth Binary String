class Solution:
    def findKthBit(self, n: int, k: int) -> str:       
        len_list = [0]*(n+1)
        len_list[1] = 1
        for i in range(1, n+1):
            len_list[i] = 2*len_list[i-1] + 1
        
        def dfs(n, k):
            mid = len_list[n-1] + 1
            if k == 1: return 0 
            elif k == 2: return 1
            elif k < mid: # if k in the first half, go up
                return dfs(n-1, k)
            elif k == mid: # if k equals mid, return 1
                return 1
            else: # if k in the second half, go up and k equals its counterpart
                return 1 - dfs(n-1, mid-(k-mid))
        return str(dfs(n, k))
