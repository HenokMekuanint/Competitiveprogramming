class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dicti=defaultdict(int)
        st=[]
        rtn=[]
        def bin_search(target,arr):
            ans=float("inf")
            left=0
            right=len(arr)-1
            while left<=right:
                
                mid=((left+right)//2)
                if target>arr[mid]:
                    left=mid+1
                elif target<arr[mid]:
                    ans=arr[mid]
                    right=mid-1
                else:
                    ans=arr[mid]
                    break
            return ans
            
        for i in range(len(intervals)):
            dicti[intervals[i][0]]=i
            st.append(intervals[i][0])
        st.sort()
        for start ,end in intervals:
            temp=bin_search(end,st)
            if temp==float("inf"):
                rtn.append(-1)
            else:
                rtn.append(dicti[temp])
        return rtn
        