class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stack=[]
        sum_of_min_time=0
        
        for color in range(len(colors)):
            if ( stack and colors[stack[-1]]==colors[color] and neededTime[color] > neededTime[stack[-1]] ):
                sum_of_min_time+= neededTime[stack[-1]]
                stack.pop()
                stack.append(color)
                
            elif ( stack and neededTime[color] <= neededTime[stack[-1]] and colors[stack[-1]]==colors[color]):
                sum_of_min_time+=neededTime[color]

            else:
                stack.append(color)
        return sum_of_min_time
