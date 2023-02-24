class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in range(len(logs)):
            if logs[i][0]!=".":
                stack.append(logs[i])
            elif logs[i]=="../" and stack:
                stack.pop()
        return len(stack)