class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr)<3:
            return False
        index=float("inf")
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                index=i
        if index==float("inf"):
            return False
        left=right=index
        while left>0:
            if arr[left-1]<arr[left]:
                left-=1
            else:
                return False
        while right<len(arr)-1:
            if arr[right]>arr[right+1]:
                right+=1
            else:
                return False
        return True

                
            
        