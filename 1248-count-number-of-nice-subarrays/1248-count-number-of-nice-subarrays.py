class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]=nums[i]%2
        total=0
        dicti=defaultdict(int)
        counter=0
        dicti[0]=1
        for i in range(len(nums)):
            total+=nums[i]
            counter+=dicti[total-k]
            dicti[total]+=1
        return counter
            