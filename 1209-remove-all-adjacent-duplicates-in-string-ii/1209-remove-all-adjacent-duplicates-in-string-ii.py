class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
      
            if not stack or stack[-1][0] != char:
                stack.append((char, 1))  
            else:
                _, count = stack.pop()  
                count += 1  


                if count < k:
                    stack.append((char, count))

        result = ""
        for char, count in stack:
            result += char * count 
        return result

