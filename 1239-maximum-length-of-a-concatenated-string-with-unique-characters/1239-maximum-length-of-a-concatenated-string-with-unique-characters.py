class Solution:
    def maxLength(self, arr: List[str]) -> int:
        temp=0
        ans=[]
        rtn=[0]
        def back_track(temp,index):
            if sorted(list(set(temp)))==sorted(list(temp)) :
                rtn[0]=max(rtn[0],len(temp))
            if index==len(arr):
                return
            else:
                for i in range(index,len(arr)):
                    back_track(temp+arr[i],i+1)
        back_track("",0)
        return rtn[0]
            
        