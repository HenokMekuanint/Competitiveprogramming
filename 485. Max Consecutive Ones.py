class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dictionary=defaultdict(int)
        maximum=0
        for i in range(len(nums)):
            if nums[i]==1:
                dictionary[1]+=1
                maximum=max(dictionary[1],maximum)
            else:
                dictionary[1]=0
        return maximum
