class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixproduct=[1]
        postfixporduct=[i for i in range(len(nums))]
        output=[i for i in range(len(nums))]
        total=1
        for i in range(len(nums)):
            total*=nums[i]
            prefixproduct.append(total)
        total=1
        for i in range(len(nums)-1,-1,-1):
            total*=nums[i]
            postfixporduct[i]=total
        postfixporduct.append(1)
        for i in range(len(nums)):
            output[i]=prefixproduct[i]*postfixporduct[i+1]
        return output
                
