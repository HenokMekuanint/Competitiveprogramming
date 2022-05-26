class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        numbers = nums
        numbers.sort()
        
        moves = 0
        
        for i in range (len(numbers) - 1):
            
            if (numbers[i + 1] <= numbers[i]):
                
                moves += (numbers[i] - numbers[i+1] + 1)
                numbers[i+1] +=  (numbers[i] - numbers[i+1] + 1)
                     
        return moves
                    
        
