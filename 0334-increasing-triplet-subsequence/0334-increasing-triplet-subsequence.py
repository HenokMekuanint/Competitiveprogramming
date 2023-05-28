class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = float('inf')
        second = float('inf')
        third = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                print(first,second,third)
                return True

        return False
                
            
                
                
            
        