class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dicti=defaultdict(int)
        for i in range(len(nums)):
            dicti[nums[i]]=i
        for pair in operations:
            nums[dicti[pair[0]]]=pair[1]
            index=dicti[pair[0]]
            del dicti[pair[0]]
            dicti[pair[1]]=index
        return nums
        