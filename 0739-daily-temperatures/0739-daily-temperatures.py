class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans=[0 for i in range(len(temp))]
        
        stack=[]
        for i in range(len(temp)):
            while stack and temp[stack[-1]]<temp[i]:
                poppedindex=stack.pop()
                ans[poppedindex]=i-poppedindex
            stack.append(i)
        return ans