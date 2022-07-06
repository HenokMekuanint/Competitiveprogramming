class Solution:
    def fizzBuzz(self, n) -> List[str]:
        
        input = []
        
        for i in range(1,n+1):  
        
            if i % 3 == 0 and i % 5 == 0:
                input.append("FizzBuzz")           
            elif i % 3 == 0:                
                input.append("Fizz")            
            elif i % 5 == 0:
                input.append("Buzz")
            else:
                input.append(str(i))
                
        return input
