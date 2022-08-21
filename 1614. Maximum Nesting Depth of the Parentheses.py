class Solution:
    def maxDepth(self, string: str) -> int:    
        stack=[]
        dict={")":"("}
        max1=0
        max2=0
        for close in  range(len(string)):
            if string[close] in dict.values():
                stack.append(string[close])
                max1=max1+1
                if max1>max2:
                    max2=max1
            elif stack and string[close] in dict and stack[-1]==dict[string[close]]:
                stack.pop()
                max1=max1-1
        return max2
