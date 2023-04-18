class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left=0
        right=len(arr)-1
        while left<right:
            mid=(left+right)//2
            
            if arr[mid-1]<arr[mid]<arr[mid+1]:
                left=mid
            elif arr[mid-1]>arr[mid]>arr[mid+1]:
                right=mid
            else:
                return mid
        