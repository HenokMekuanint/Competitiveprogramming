class Solution:
    def decodeString(self, s: str) -> str:
        if s.isdigit():
            return ""
        stack=[]
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                char_temp=""
                while stack[-1]!="[":
                    char_temp=stack.pop()+char_temp
                stack.pop()
                k=""
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                stack.append(int(k)*char_temp)
        return "".join(stack)
                    
                    
                
                
                
                
                
                
        
        