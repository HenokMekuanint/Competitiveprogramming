class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightmax=-1
        for i in range(len(arr)-1,-1,-1):
            newmax=max(arr[i],rightmax)
            arr[i]=rightmax
            rightmax=newmax
        return arr
        
                
        