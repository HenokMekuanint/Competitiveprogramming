class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr1=[]
        arr2=[]
        arr3=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                arr1.append(nums[i])
            elif nums[i]>pivot:
                arr2.append(nums[i])
            elif nums[i]==pivot:
                arr3.append(nums[i])
        return arr1+arr3+arr2
                
        
        
        