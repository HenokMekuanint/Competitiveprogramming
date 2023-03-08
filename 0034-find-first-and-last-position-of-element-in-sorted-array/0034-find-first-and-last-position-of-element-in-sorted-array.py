class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if target<nums[mid]:
                right=mid-1
            elif target>nums[mid]:
                left=mid+1
            else:
                while nums[left]!=target:
                    left+=1
                ans[0]=left
                while nums[right]!=target:
                    right-=1
                ans[1]=right
                break
        return ans
                
                
        
        