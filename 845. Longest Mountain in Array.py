class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        #[2,1,4,7,2,5]
        ans=0
        
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                j=i
                counter=1
                while(j>0 and arr[j]>arr[j-1]):
                    counter+=1
                    j-=1
                j=i
                while(j<len(arr)-1 and arr[j]>arr[j+1]):
                    counter+=1
                    j+=1
                ans=max(ans,counter)
            else:
                continue
        return ans
                
