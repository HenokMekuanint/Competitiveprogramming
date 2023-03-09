class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        res=float("inf")
        
        def combination(index,arr):
            nonlocal res
            if index==len(cookies):
                if min(arr)!=0:
                    res=min(max(arr),res)
                return
            for i in range(len(arr)):
                new_arr=arr[::]
                new_arr[i]+=cookies[index]
                if new_arr.count(0)>len(cookies)-(index+1):
                    continue
                combination(index+1,new_arr)
        combination(0,[0]*k)
        return res
            
        
        
        