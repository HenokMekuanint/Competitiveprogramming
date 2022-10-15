class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0
        end=0
        maxlen=0
        flippedOnes=0
        while end<len(nums):
            if nums[end]==1:
                end+=1
            elif nums[end]==0:
                while flippedOnes>=k:
                    if nums[start]==0:
                        flippedOnes-=1
                    start+=1
                if flippedOnes<k:
                    flippedOnes+=1
                    end+=1

            maxlen=max(maxlen,end-start)
        return maxlen
