class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total=0
        dicti=defaultdict(int)
        count=0
        dicti[0]=1
        for num in nums:
            total+=num
            count+=dicti[total-goal]
            dicti[total]+=1
        return count
            