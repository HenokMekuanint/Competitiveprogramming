class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        nums=list(map(int,str(n)))

        index1=len(nums)-2

        while index1>=0 and nums[index1]>=nums[index1+1]:
            index1-=1
        if index1==-1:
            return -1
        index2=len(nums)-1

        while nums[index2]<=nums[index1]:
            index2-=1

        nums[index2],nums[index1]=nums[index1],nums[index2]
        nums[index1+1:]=reversed(nums[index1+1:])

        res=""
        for num in nums:
            res+=str(num)
        res=int(res)
        return res if res < 2 ** 31 else -1 
