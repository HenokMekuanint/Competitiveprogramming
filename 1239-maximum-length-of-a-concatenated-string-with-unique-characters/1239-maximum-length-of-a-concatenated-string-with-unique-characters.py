class Solution:
    def maxLength(self, arr: List[str]) -> int:
        temp=0
        ans=[]
        rtn=0
        def back_track(temp,index):
            if temp:
                ans.append(temp)
            if index==len(arr):
                return
            else:
                for i in range(index,len(arr)):
                    back_track(temp+arr[i],i+1)
        back_track("",0)
        for ch in ans:
            if sorted(list(set(ch)))==sorted(list(ch)):
                rtn=max(rtn,len(ch))
        return rtn
            
        