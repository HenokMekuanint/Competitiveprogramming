class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        array=[]
        nums.sort()

        for index in range(len(nums)):
            if nums[index]==target:
                array.append(index)
        return array
