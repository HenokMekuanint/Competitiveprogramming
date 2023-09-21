class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        pivot=float('inf')
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                pivot=i
        
        if  pivot==float('inf'):
            return False
        left=pivot
        right=pivot
        while left>0:
            if arr[left]>arr[left-1]:
                left-=1
            else:
                return False
        while right<len(arr)-1:
            if arr[right]>arr[right+1]:
                right+=1
            else:
                return False
        return True
        