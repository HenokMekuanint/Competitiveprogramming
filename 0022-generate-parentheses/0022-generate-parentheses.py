class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans=[]
        def back_track(stack,parent):
            if len(parent)>2*n:
                return
            if len(parent)==2*n and not stack:
                ans.append(parent)
                return
            
            if len(stack)<n:
                back_track(stack+["("],parent+"(")
            if stack:
                stack.pop()
                back_track(stack,parent+")")
            return
        back_track(["("],"(")
        return ans