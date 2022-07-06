<<<<<<< HEAD
def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []

        for i in range(1,n+1):

            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)

            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            elif divisible_by_3:
                ans.append("Fizz")
            elif divisible_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(i))

        return ans
=======
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
>>>>>>> a5ee5542be08b3b99e1456b3d44544b177d9a53f
