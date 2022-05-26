class Solution:
    def reverseParentheses(self, s: str) -> str:
        stringChars = []
        st = []
        for i in s :
            stringChars.append(i)

        for i in range (len(stringChars)):
            charsToReverse =[]
            if stringChars[i] == ")":
                u = st[-1]
                st.pop(-1)
                if u == "(":
                    continue
                charsToReverse.append(u)
                while len(st):
                    u = st[-1]
                    if u == "(":
                        st.pop(-1)
                        break
                    st.pop(-1)
                    charsToReverse.append(u)

                for i in charsToReverse:
                    st.append(i)
            else: 
                st.append(stringChars[i] )

        result = "".join(st) 
        return result
        
