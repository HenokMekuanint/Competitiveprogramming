class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans=0
        temp=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                ans+=1
                temp.append(nums[i])
        for i in range(len(temp)):
            nums[i]=temp[i]
        for i in range(len(temp),len(nums)):
            nums[i]="_"
        return ans
        