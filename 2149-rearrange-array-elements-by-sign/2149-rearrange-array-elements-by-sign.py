class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)
        for i in range(len(pos)+len(neg)):
            if i%2==0:
                nums[i]=pos.pop(0)
            else:
                nums[i]=neg.pop(0)
        return nums
                
        