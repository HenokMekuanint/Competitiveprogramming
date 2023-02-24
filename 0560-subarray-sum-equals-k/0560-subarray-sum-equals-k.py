class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dicti=defaultdict(int)
        total=0
        counter=0
        dicti[0]=1
        for num in (nums):
            total+=num
            counter+=dicti[total-k]
            dicti[total]+=1
        return counter
            