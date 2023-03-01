class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        freq=defaultdict(int)
        visited=defaultdict(bool)
        for i in range(len(s)):
            freq[s[i]]+=1
            if s[i] not in visited:
                visited[s[i]]=False
        
        for i in range(len(s)):
            
            if visited[s[i]]:
                freq[s[i]]-=1
                continue
            else:
                while stack and stack[-1]>ord(s[i]) and freq[chr(stack[-1])]>0:
                   
                    visited[chr(stack[-1])]=False
                    stack.pop()
                stack.append(ord(s[i]))
                visited[s[i]]=True
                freq[s[i]]-=1
        return "".join([chr(item) for item in stack])