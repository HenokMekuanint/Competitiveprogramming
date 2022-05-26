class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ordered = []
        largest = 0
        start = 0
        end = len(nums) - 1
        while start < end:
            sublist = []
            sublist.append(nums[start])
            sublist.append(nums[end])
            start += 1
            end -= 1
            ordered.append(sublist)

        for i in ordered:
            if (i[0]+i[1]) > largest:
                largest = i[0] + i[1]

        return largest
        
        
