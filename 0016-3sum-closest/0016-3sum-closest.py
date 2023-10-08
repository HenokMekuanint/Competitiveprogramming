class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        
        nums.sort()
        ans=float("inf")
        diff=float("inf")
        for i in range(len(nums)):
            targ=target
            two_sum=targ-nums[i]
            left=i+1
            right=len(nums)-1
            while left<right:
                
                cur_sum=nums[left]+nums[right]
                if diff>abs(target-(nums[i]+nums[left]+nums[right])):
                    ans=nums[i]+nums[left]+nums[right]
                    diff=abs(target-(nums[i]+nums[left]+nums[right]))
                if cur_sum>two_sum:
                    right-=1
                    
                elif cur_sum<two_sum:
                    left+=1
                else:
                    return target
        return ans
            