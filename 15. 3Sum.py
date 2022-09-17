class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        array=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            L=i+1
            R=len(nums)-1
            while L<R:
                threesum=a+nums[L]+nums[R]
                if threesum>0:
                    R-=1
                elif threesum <0 :
                    L+=1
                else:
                    array.append([a,nums[L],nums[R]])
                    L+=1
                    while nums[L]==nums[L-1] and L<R:
                        L+=1
        return array
