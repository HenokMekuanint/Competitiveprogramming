class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators = ['+', '-', '*', '/']
        for num in tokens:
            if num not in operators:
                stack.append(int(num))
            elif  len(stack)>1:
                num2=stack.pop()
                num1=stack.pop()
                if num=="+": stack.append(num1+num2)
                if num=="-": stack.append(num1-num2)
                if num=="*": stack.append(num1*num2)
                if num=="/":
                    if -1<num1/num2<1:
                       stack.append(0) 
                    else: 
                        stack.append(int(num1/num2))
        return stack[0]