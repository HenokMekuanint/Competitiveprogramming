class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ones = 0
        twos = 0

        for num in nums:
            twos = twos | (ones & num)
            ones = ones ^ num
            common_bit_mask = ~(ones & twos)
            ones = ones & common_bit_mask
            twos = twos & common_bit_mask

        return ones
        