class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # maximum=0
        # maximum=right-left
        # [0,1,1,1,0,1,1,0,1]  zerocounter=2
        #    L
        #              R
        
        maximum=0
        zerocounter=0
        left=0
        
        for right in range(len(nums)):
            if nums[right]==0:
                zerocounter+=1
            while zerocounter>1:
                if nums[left]==0:
                    zerocounter-=1
                left+=1
            maximum=max(right-left,maximum)
        return maximum
