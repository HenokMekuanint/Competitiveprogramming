class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={")":"(","}":"{","]":"["}
        for close in s:
            if close in mapping:
                if stack and stack[-1] == mapping[close]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(close)
        return True if len(stack)==0 else False
