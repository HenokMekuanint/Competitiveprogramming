class Solution:
    def calculate(self, s: str) -> int:
        import math
        st = []
        ops = ['+','-','/','*']
        noSpace = []

        for i in range ((len(s))):
            if s[i] != ' ':
                noSpace.append(s[i])

        s = ''.join(noSpace)
        i = 0
        while  i < len(s):
            if s[i] == '*':
                operand1 = st.pop()
                k = i + 1
                while k < len(s) and s[k] not in ops :
                    k += 1
                st.append(int(operand1) * int(s[i + 1:k ]))
                if k == len(s)-1:
                    break
                i = k 

            elif s[i] == '/':
                operand1 = st.pop()
                k = i + 1
                while k < len(s) and s[k] not in ops:
                    k += 1 
                st.append(math.trunc(int(operand1) / int(s[i + 1:k ])))
                if k == len(s):
                    break
                i = k 

            elif s[i] == '-':
                k = i + 1
                while k < len(s) and s[k] not in ops:
                    k += 1 
                st.append(-int(s[i + 1:k ]))
                if k == len(s):
                    break
                i = k

            elif s[i] == '+':
                k = i + 1
                while k < len(s) and s[k] not in ops:
                    k += 1 
                st.append(int(s[i + 1:k ]))
                if k == len(s):
                    break
                i = k

            elif s[i] not in ops:
                j = i 
                while j < len(s) and s[j] not in ops:
                    j += 1
                st.append(int(s[i:j]))
                if j == len(s):
                    break
                i = j 

        answer = 0
        for i in range(len(st)):
            answer += st[i]
        return answer
                
        

       

