class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total=0
        dicti=defaultdict(int)
        dicti[0]=1
        counter=0
        for i in range(len(nums)):
            total+=nums[i]
            counter+=dicti[total%k]
            dicti[total%k]+=1
        return counter
        