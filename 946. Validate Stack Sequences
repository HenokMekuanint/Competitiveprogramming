class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        st = []
        while i < len(pushed):
            st.append(pushed[i])
            i+=1
            
            while j < len(popped) and st:
                if st[-1] == popped[j]:
                    st.pop()
                    j += 1
                else:
                    break

        if st:
            return False
        
        return True
