class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictionary=defaultdict(int)
        count=0
        total=0
        dictionary[0]=1
        for num in nums:
            total+=num
            count+=dictionary.get(total-k,0)
            dictionary[total]+=1
        return count
