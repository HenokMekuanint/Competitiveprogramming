class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
#         [2,2,2,2,5,5,5,8] k=3 treshold=4
#          L
#              R
                
        
        left=0
        windowsum=0
        counter=0
        for right in range(len(arr)):
            windowsum+=arr[right]
            while (right-left+1)==k:
                if windowsum/k>=threshold: counter+=1
                windowsum-=arr[left]
                left+=1
        return counter
